"""Batched triage + dedupe + TLDR over any OpenAI-compatible chat endpoint.

Default is GitHub Models, which is free from Actions using the workflow's own
GITHUB_TOKEN. Its free tier caps each request at ~8k input / 4k output tokens,
hence small batches and short snippets. Items are judged exactly once
(seen-state) and obvious junk never reaches the model.
"""

from __future__ import annotations

import json
import logging
import os
import re
import time

import requests

from .models import Cluster

log = logging.getLogger(__name__)

CATEGORIES = ["vulnerability", "exploitation", "supply_chain", "breach", "outage", "malware", "advisory", "other"]

SYSTEM = """You edit a security signal feed read by experienced security engineers. Readers trust it because it is boring and correct: nothing hyped, nothing they would regret missing.

For every candidate, decide:

verdict: "signal" only if a competent security engineer at a typical organization would want to know about it today. That usually means:
- a vulnerability in widely deployed software, hardware or cloud services with serious impact (pre-auth RCE, auth bypass, privilege escalation to root/SYSTEM/admin, cross-tenant access), especially if exploited, weaponized or trivially exploitable;
- confirmed exploitation in the wild, zero-days, emergency patches;
- supply-chain compromise of popular packages, build systems or vendors;
- confirmed breaches or incidents with a large blast radius (identity providers, cloud/SaaS platforms, MSPs, critical infrastructure, tens of millions of people);
- major outages caused by attacks or bad security updates;
- emergency government directives or urgent joint advisories.
Everything else is "noise": marketing, funding, M&A, opinion, listicles, webinars, product launches, surveys and reports, generic phishing or scam campaigns, arrests and court cases, vulnerabilities in niche or rarely deployed software, research without practical impact, and stories that repeat an already-covered item without new material facts. When in doubt, it is noise.

Candidates marked "KEV: yes" are in CISA's Known Exploited Vulnerabilities catalog, so exploitation is confirmed; treat them as signal unless the product is genuinely obscure.

duplicate_of: if the candidate is the same story (same vulnerability, incident or campaign, however worded) as an already-covered item or an earlier candidate, give that id (e.g. "p3" or "c2"); otherwise "".

importance: integer 0-10. 9-10 drop everything (mass exploitation of widely deployed internet-facing systems, major supply-chain compromise). 7-8 act this week. 5-6 worth knowing. Below 5 is noise.

exploited: true only if the text says in-the-wild exploitation is confirmed, or the item is KEV.

category: one of """ + ", ".join(CATEGORIES) + """.

headline: neutral and specific, at most 90 characters: product, issue, status. No clickbait.

tldr: signal only, else "". One or two plain sentences: what it is, who is affected (product and versions when given), status (exploited / public PoC / patched). Use only facts present in the text; never guess versions, numbers or attribution.

action: signal only, else "". The concrete step a defender should take, at most 20 words, e.g. "Upgrade FortiWeb to 7.4.8+ and audit for unknown admin accounts." "" if nothing is actionable.

Respond with only a JSON object, one entry per candidate id:
{"items": [{"id": "c1", "verdict": "noise", "duplicate_of": "", "importance": 2, "exploited": false, "category": "other", "headline": "...", "tldr": "", "action": ""}]}"""


def http_post(url: str, headers: dict, body: dict) -> dict:
    r = requests.post(url, headers=headers, json=body, timeout=120)
    r.raise_for_status()
    try:
        return r.json()
    except ValueError:
        raise ValueError(f"non-JSON response (HTTP {r.status_code}, {r.headers.get('content-type')}): {r.text[:300]!r}") from None


def _truncate(s: str, n: int) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def render_candidate(c: Cluster, snippet: int) -> str:
    meta = ["sources: " + ", ".join(sorted({i.source for i in c.items}))]
    cves = c.cves
    if cves:
        meta.append("CVEs: " + ", ".join(cves[:6]) + (" …" if len(cves) > 6 else ""))
    if c.cvss:
        meta.append(f"CVSS {c.cvss:.1f}")
    if c.epss is not None:
        meta.append(f"EPSS {c.epss:.2f}")
    if c.kev:
        meta.append("KEV: yes")
    lines = [f"[{c.cid}] " + " | ".join(meta)]
    for it in c.ordered()[:3]:
        lines.append(f"- {it.title}")
        if it.text:
            lines.append(f"  {_truncate(it.text, snippet)}")
    return "\n".join(lines)


def _parse(content: str) -> list[dict]:
    # Some providers wrap JSON in a code fence even in JSON mode.
    content = re.sub(r"^```(?:json)?\s*|\s*```$", "", content.strip())
    data = json.loads(content)
    return data.get("items", []) if isinstance(data, dict) else data


def _apply(c: Cluster, v: dict) -> None:
    c.verdict = "signal" if v.get("verdict") == "signal" else "noise"
    c.duplicate_of = str(v.get("duplicate_of") or "").strip()
    try:
        c.importance = max(0, min(10, int(v.get("importance", 0))))
    except (TypeError, ValueError):
        c.importance = 0
    c.exploited = v.get("exploited") is True
    c.category = v.get("category") if v.get("category") in CATEGORIES else "other"
    c.headline = str(v.get("headline") or c.ordered()[0].title).strip()[:140]
    c.tldr = str(v.get("tldr") or "").strip()
    c.action = str(v.get("action") or "").strip()


def triage(clusters: list[Cluster], covered: list[str], cfg: dict, post=http_post) -> list[Cluster]:
    """Judge clusters in place. Returns the ones that got a verdict; the rest are retried next run."""
    llm = cfg["llm"]
    url = llm["base_url"].rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}
    if os.environ.get(llm.get("api_key_env", "")):
        headers["Authorization"] = f"Bearer {os.environ[llm['api_key_env']]}"
    for n, c in enumerate(clusters, 1):
        c.cid = f"c{n}"

    covered = list(covered)[:40]  # newest first; keeps the prompt inside small free-tier windows
    judged: list[Cluster] = []
    tokens_in = tokens_out = 0
    size = llm["batch_size"]
    for start in range(0, len(clusters), size):
        if start:
            time.sleep(llm["min_interval_s"])
        chunk = clusters[start : start + size]
        prompt = (
            "Already covered (for duplicate_of):\n" + ("\n".join(covered) or "(none)")
            + "\n\nCandidates:\n\n" + "\n\n".join(render_candidate(c, llm["snippet_chars"]) for c in chunk)
            + "\n\nReturn the JSON object."
        )
        body = {
            "model": llm["model"],
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        }
        try:
            resp = post(url, headers, body)
            choice = resp["choices"][0]
            content = choice["message"].get("content") or ""
            try:
                parsed = _parse(content)
            except ValueError:
                raise ValueError(f"model reply is not JSON (finish_reason={choice.get('finish_reason')}): {content[:300]!r}") from None
            verdicts = {str(v.get("id")): v for v in parsed if isinstance(v, dict)}
        except requests.HTTPError as e:
            status = e.response.status_code if e.response is not None else "?"
            detail = e.response.text[:300] if e.response is not None else ""
            log.error("LLM HTTP %s for %d candidates, will retry next run: %s", status, len(chunk), detail)
            if status in (401, 403, 404, 429):  # auth, unknown model or rate limit: later chunks will fail too
                break
            continue
        except (requests.RequestException, KeyError, IndexError, ValueError) as e:
            log.error("LLM call/parse failed for %d candidates, will retry next run: %s", len(chunk), e)
            continue

        usage = resp.get("usage") or {}
        tokens_in += usage.get("prompt_tokens", 0)
        tokens_out += usage.get("completion_tokens", 0)
        if choice.get("finish_reason") == "length":
            log.warning("LLM output truncated; lower llm.batch_size")
        for c in chunk:
            if c.cid in verdicts:
                _apply(c, verdicts[c.cid])
                judged.append(c)
                if c.verdict == "signal" and not c.duplicate_of:
                    covered.append(f"[{c.cid}] {c.headline}")

    log.info("LLM %s: %d/%d judged, %d in / %d out tokens", llm["model"], len(judged), len(clusters), tokens_in, tokens_out)
    return judged
