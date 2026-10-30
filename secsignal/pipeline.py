"""Clustering, cheap deterministic filtering and scoring. No network, no LLM."""

from __future__ import annotations

import re
from collections import defaultdict

from .models import Cluster, Item

# A news item citing more CVEs than this is a roundup (Patch Tuesday etc.);
# letting it bridge clusters would glue unrelated vulns together.
MAX_BRIDGE_CVES = 3

STRONG = re.compile(
    r"zero[- ]day|0-day|actively exploited|exploited in (the wild|attacks)|under (active )?attack|"
    r"mass exploitation|remote code execution|\bRCE\b|auth(entication)? bypass|supply[- ]chain|"
    r"backdoor|compromised|breach|emergency (patch|directive)|wormable",
    re.I,
)


def cluster(items: list[Item]) -> list[Cluster]:
    parent = list(range(len(items)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    owner: dict[str, int] = {}
    for idx, it in enumerate(items):
        if len(it.cves) > MAX_BRIDGE_CVES:
            continue
        for cve in it.cves:
            if cve in owner:
                parent[find(idx)] = find(owner[cve])
            else:
                owner[cve] = idx

    groups: dict[int, list[Item]] = defaultdict(list)
    for idx, it in enumerate(items):
        groups[find(idx)].append(it)
    return [Cluster(items=g) for g in groups.values()]


WORD_RE = re.compile(r"[a-z0-9][a-z0-9.\-]{2,}")
# Words every security headline shares; overlap on these alone says nothing.
GENERIC = set(
    """the and for with from that this into over after amid about warns warn says said new now its are has have
    been was were will can could may hackers hacker attackers attack attacks attacked flaw flaws bug bugs vulnerability
    vulnerabilities critical severe security patch patches patched fixes fixed fix update updates exploited exploit
    exploits exploitation zero-day zero day actively wild active breach breached data million millions users customers
    company firm confirms confirmed disclosed discloses reports report researchers cyberattack ransomware gang group
    malware campaign steal stole stolen affecting affected impacts impact remote code execution rce cve""".split()
)


def title_words(title: str) -> set[str]:
    return {w.strip(".-") for w in WORD_RE.findall(title.lower())} - {""}


def same_story(a: set[str], b: set[str]) -> bool:
    shared = a & b
    distinct = shared - GENERIC
    if len(distinct) >= 2:  # e.g. "fortinet" + "fortiweb"
        return True
    return bool(distinct) and len(shared) >= 3 and len(shared) / min(len(a), len(b)) >= 0.5


def merge_similar_titles(clusters: list[Cluster]) -> list[Cluster]:
    """Collapse the same story told by different outlets (no shared CVE to join on)."""
    out: list[tuple[Cluster, list[set[str]]]] = []
    for c in clusters:
        words = [title_words(i.title) for i in c.items if i.kind == "news"]
        target = next((t for t, tw in out if words and any(same_story(w, x) for w in words for x in tw)), None)
        if target is None:
            out.append((c, words))
        else:
            target.items.extend(c.items)
            next(tw for t, tw in out if t is target).extend(words)
    return [c for c, _ in out]


def compile_terms(terms: list[str]) -> re.Pattern | None:
    if not terms:
        return None
    return re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b", re.I)


def compile_any(patterns: list[str]) -> re.Pattern | None:
    return re.compile("|".join(f"(?:{p})" for p in patterns), re.I) if patterns else None


def watch_text(it: Item) -> str:
    # News bodies name-drop vendors in passing, so only trust their titles.
    return it.title if it.kind == "news" else f"{it.title} {it.text[:300]}"


def prefilter(clusters: list[Cluster], cfg: dict) -> tuple[list[Cluster], list[Cluster]]:
    """Split into (candidates, dropped). Drops only clusters where every item is obvious junk."""
    f = cfg["filters"]
    watch = compile_terms(f.get("watchlist", []))
    noise_title = compile_any(f.get("noise_title", []))
    noise_text = compile_any(f.get("noise_text", []))

    def junk(it: Item) -> bool:
        if it.kind == "news":
            return bool(noise_title and noise_title.search(it.title))
        if it.kind in ("nvd", "ghsa"):
            return bool(noise_text and noise_text.search(f"{it.title} {it.text}"))
        return False

    keep, drop = [], []
    for c in clusters:
        if watch:
            hit = next((m.group(0) for it in c.items if (m := watch.search(watch_text(it)))), "")
            c.watch_hit = hit.lower()
        if c.kev or c.watch_hit or not all(junk(i) for i in c.items):
            keep.append(c)
        else:
            drop.append(c)
    return keep, drop


def prior(c: Cluster) -> int:
    """Signal before any judgement; used to rank candidates and as score bonuses."""
    s = 0
    if c.kev:
        s += 15
    if (c.epss or 0) >= 0.5:
        s += 5
    n = len(c.news_sources)
    s += 10 if n >= 3 else 5 if n == 2 else 0
    if c.watch_hit:
        s += 5
    if (c.cvss or 0) >= 9:
        s += 3
    return s


def heuristic_triage(clusters: list[Cluster]) -> None:
    """Free fallback when no LLM is configured: keyword + metadata rules."""
    for c in clusters:
        lead = c.ordered()[0]
        blob = " ".join(f"{i.title} {i.text}" for i in c.items)
        strong = bool(STRONG.search(blob))
        if c.kev:
            c.importance = 7
        elif strong and (c.watch_hit or len(c.news_sources) >= 2):
            c.importance = 7
        elif strong or (c.watch_hit and (c.cvss or 0) >= 9):
            c.importance = 6
        else:
            c.importance = 3
        c.verdict = "signal" if c.importance >= 5 else "noise"
        c.exploited = c.kev or bool(re.search(r"exploited|in the wild|zero[- ]day", blob, re.I))
        c.headline = lead.title[:120]
        c.tldr = " ".join(re.split(r"(?<=[.!?])\s", lead.text)[:2])[:400]
        kev = next((i for i in c.items if i.kind == "kev"), None)
        if kev and (m := re.search(r"Required action: (.*?)(?: Federal due date|$)", kev.text)):
            c.action = m.group(1).strip()


def merge_duplicates(clusters: list[Cluster]) -> list[Cluster]:
    """Fold clusters the LLM flagged as duplicate_of another candidate (c#) into it."""
    by_cid = {c.cid: c for c in clusters}
    for c in clusters:
        target, hops = by_cid.get(c.duplicate_of), 0
        while target is not None and target.duplicate_of in by_cid and hops < 5:
            target, hops = by_cid[target.duplicate_of], hops + 1
        if target is not None and target is not c:
            target.items.extend(c.items)
            c.items = []
    return [c for c in clusters if c.items]


def score(c: Cluster, cfg: dict) -> str:
    """Set c.score and return the tier: 'act', 'watch' or '' (dropped)."""
    run = cfg["run"]
    if c.kev:
        c.importance = max(c.importance, 5)  # CISA-confirmed exploitation always surfaces
        c.verdict = "signal"
        c.exploited = True
    if c.verdict != "signal":
        c.score = 0
        return ""
    c.score = min(100, c.importance * 8 + prior(c) + (5 if c.exploited and not c.kev else 0))
    if c.score >= run["act_score"]:
        return "act"
    if c.score >= run["watch_score"]:
        return "watch"
    return ""
