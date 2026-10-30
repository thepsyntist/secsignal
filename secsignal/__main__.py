"""secsignal: fetch → dedupe → cluster → filter → triage/TLDR → score → publish.

    python -m secsignal               # full run (LLM if its token/key is set)
    python -m secsignal --dry-run     # print what would be published, change nothing
    python -m secsignal --no-llm      # free heuristic mode
"""

from __future__ import annotations

import argparse
import logging
import os
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import llm, output, pipeline, sources
from .models import Cluster
from .state import Store

log = logging.getLogger("secsignal")
ROOT = Path(__file__).resolve().parent.parent


def load_config(path: Path) -> dict:
    cfg = tomllib.loads(path.read_text())
    cfg.setdefault("feeds", [])
    return cfg


def to_entry(c: Cluster, tier: str, now: datetime) -> dict:
    stamp = now.isoformat(timespec="seconds")
    return {
        "key": c.key,
        "tier": tier,
        "score": c.score,
        "headline": c.headline,
        "tldr": c.tldr,
        "action": c.action,
        "category": c.category,
        "exploited": c.exploited,
        "kev": c.kev,
        "cves": c.cves,
        "cvss": c.cvss,
        "epss": c.epss,
        "watch": c.watch_hit,
        "links": c.links(),
        "first_seen": stamp,
        "updated": stamp,
    }


def attach(entry: dict, c: Cluster, now: datetime) -> bool:
    """Fold a follow-up story into an already-published entry. True if it now deserves a fresh alert."""
    known = {l["url"] for l in entry["links"]}
    entry["links"] += [l for l in c.links() if l["url"] not in known]
    entry["cves"] = sorted(set(entry["cves"]) | set(c.cves))
    entry["updated"] = now.isoformat(timespec="seconds")
    if c.kev and not entry["kev"]:
        entry.update(kev=True, exploited=True, tier="act", headline=f"Now exploited: {entry['headline']}")
        return True
    return False


def run(cfg: dict, root: Path, use_llm: bool, do_push: bool, dry_run: bool, now: datetime | None = None, post=None) -> list[dict]:
    now = now or datetime.now(timezone.utc)
    since = now - timedelta(hours=cfg["run"]["lookback_hours"])
    store = Store(root)

    items, _ = sources.fetch_all(cfg, since, now)
    fresh = list({i.id: i for i in items if i.id not in store.seen}.values())
    sources.enrich_epss(fresh)

    candidates, dropped = pipeline.prefilter(pipeline.merge_similar_titles(pipeline.cluster(fresh)), cfg)
    candidates.sort(key=pipeline.prior, reverse=True)
    cap = cfg["run"]["max_candidates"]
    dropped += candidates[cap:]
    candidates = candidates[:cap]
    store.mark_seen((i.id for c in dropped for i in c.items), now)

    # Follow-ups to stories we already published: match on CVE before paying the LLM.
    recent = store.recent(now, cfg["run"]["dedupe_hours"])
    alerts: list[dict] = []
    pending = []
    for c in candidates:
        entry = next((e for e in recent if set(e["cves"]) & set(c.cves)), None)
        if entry:
            if attach(entry, c, now):
                alerts.append(entry)
            store.mark_seen((i.id for i in c.items), now)
        else:
            pending.append(c)
    log.info("%d fetched, %d new, %d clusters to judge, %d junk dropped", len(items), len(fresh), len(pending), len(dropped))

    if use_llm:
        covered = [f"[p{n}] {e['headline']}" for n, e in enumerate(recent, 1)]
        judged = llm.triage(pending, covered, cfg, **({"post": post} if post else {}))
        # Never let a dead endpoint silence alerts: if the LLM judged nothing, or an
        # item has waited too long for a retry, fall back to the keyword rules.
        done = {id(c) for c in judged}
        stale = now - timedelta(hours=cfg["run"]["llm_retry_hours"])
        fallback = [c for c in pending if id(c) not in done and (not judged or min(i.published for i in c.items) < stale)]
        if fallback:
            log.warning("LLM unavailable for %d clusters; using heuristic triage for them", len(fallback))
            pipeline.heuristic_triage(fallback)
            judged += fallback
    else:
        for n, c in enumerate(pending, 1):
            c.cid = f"c{n}"
        pipeline.heuristic_triage(pending)
        judged = pending
    store.mark_seen((i.id for c in judged for i in c.items), now)

    new_entries = []
    for c in pipeline.merge_duplicates(judged):
        if c.duplicate_of.startswith("p") and c.duplicate_of[1:].isdigit() and 0 < int(c.duplicate_of[1:]) <= len(recent):
            entry = recent[int(c.duplicate_of[1:]) - 1]
            if attach(entry, c, now):
                alerts.append(entry)
            continue
        tier = pipeline.score(c, cfg)
        if tier:
            new_entries.append(to_entry(c, tier, now))
    new_entries.sort(key=lambda e: -e["score"])
    alerts += new_entries

    push_tiers = {"act": {"act"}, "watch": {"act", "watch"}, "none": set()}[cfg["run"]["push_tier"]]
    to_push = [e for e in alerts if e["tier"] in push_tiers]
    log.info("published %d (%d act), pushing %d", len(new_entries), sum(e["tier"] == "act" for e in new_entries), len(to_push))

    if dry_run:
        for e in alerts:
            print(output.push_text(e), end="\n\n")
        return alerts

    store.entries = new_entries + store.entries
    store.save(now, cfg["run"]["keep_days"])
    days = {e["first_seen"][:10] for e in alerts}
    output.write_rss(store.entries, root / "out" / "feed.xml", cfg)
    output.write_markdown(store.entries, root, now, days)
    if do_push and to_push:
        output.push(to_push)
    return alerts


def main() -> None:
    ap = argparse.ArgumentParser(prog="secsignal")
    ap.add_argument("--config", type=Path, default=ROOT / "config.toml")
    ap.add_argument("--no-llm", action="store_true", help="heuristic triage only (free)")
    ap.add_argument("--no-push", action="store_true", help="don't send notifications")
    ap.add_argument("--dry-run", action="store_true", help="print alerts; don't write state, outputs or push")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    cfg = load_config(args.config)
    use_llm = not args.no_llm and cfg["llm"]["enabled"]
    key_env = cfg["llm"].get("api_key_env", "")
    if use_llm and key_env and not os.environ.get(key_env):
        log.warning("%s not set; falling back to heuristic triage", key_env)
        use_llm = False
    run(cfg, ROOT, use_llm, not args.no_push, args.dry_run)


if __name__ == "__main__":
    main()
