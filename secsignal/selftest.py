"""Live LLM check on made-up stories: `python -m secsignal --selftest`.

Sends a fixed mix of real-looking signal and obvious noise through the same
clustering, triage and scoring as a normal run, prints what the model decided,
and exits non-zero if the model judged nothing. Writes no state, pushes nothing.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from . import llm, pipeline
from .models import Item

log = logging.getLogger(__name__)
NOW = datetime.now(timezone.utc)


def _item(id, kind, source, title, text, cves=(), cvss=None, kev=False):
    return Item(id=id, kind=kind, source=source, title=title, url=f"https://example.test/{id}", text=text,
                published=NOW, cves=set(cves), cvss=cvss, kev=kev)


# (item, expected verdict) — fictional CVEs and companies.
SAMPLES = [
    (_item("kev1", "kev", "CISA KEV", "CVE-2099-0001: Fortinet FortiWeb Authentication Bypass Vulnerability",
           "Fortinet FortiWeb contains an authentication bypass that lets unauthenticated attackers create admin "
           "accounts via crafted HTTP requests. Required action: Apply vendor updates (FortiWeb 7.6.5+).",
           ["CVE-2099-0001"], 9.8, True), "signal"),
    (_item("news1", "news", "BleepingComputer", "Fortinet warns FortiWeb zero-day CVE-2099-0001 exploited in attacks",
           "Fortinet says the flaw has been exploited to create rogue admin accounts on internet-facing appliances.",
           ["CVE-2099-0001"]), "signal"),
    (_item("nvd1", "nvd", "NVD", "CVE-2099-0002: Heap overflow in OpenSSH sshd before 10.9",
           "A heap overflow in OpenSSH sshd before 10.9 allows unauthenticated remote code execution as root on "
           "default configurations. A public proof-of-concept is available.", ["CVE-2099-0002"], 9.8), "signal"),
    (_item("news2", "news", "The Record", "Nimbus Cloud confirms breach exposing 60 million customer records",
           "Nimbus Cloud said attackers used stolen support credentials to access customer databases."), "signal"),
    (_item("news3", "news", "SecurityWeek", "Hackers steal data of 60 million Nimbus Cloud users via support portal",
           "The cloud provider disclosed the intrusion on Wednesday and is resetting tokens."), "signal"),
    (_item("news4", "news", "SecurityWeek", "Acme Security launches AI-powered SOC copilot",
           "Acme Security today announced the general availability of its SOC copilot for mid-market teams."), "noise"),
    (_item("nvd2", "nvd", "NVD", "CVE-2099-0003: Stored XSS in TinyGuestbook 0.3",
           "A stored cross-site scripting issue in TinyGuestbook 0.3 allows an authenticated admin to inject script "
           "into the guestbook footer.", ["CVE-2099-0003"], 9.0), "noise"),
    (_item("news5", "news", "The Hacker News", "Survey: 70% of CISOs plan to increase identity budgets",
           "A new survey of 400 security leaders finds identity security is the top spending priority."), "noise"),
]


def run(cfg: dict) -> int:
    expected = {it.id: want for it, want in SAMPLES}
    clusters = pipeline.merge_similar_titles(pipeline.cluster([it for it, _ in SAMPLES]))
    judged = llm.triage(clusters, [], cfg)
    if not judged:
        print("FAIL: the LLM judged nothing; see errors above.")
        return 1

    ok = 0
    merged = pipeline.merge_duplicates(judged)
    for c in merged:
        tier = pipeline.score(c, cfg) or "dropped"
        wants = {expected[i.id] for i in c.items}
        want = "signal" if "signal" in wants else "noise"
        hit = (tier != "dropped") == (want == "signal")
        ok += hit
        print(f"\n{'PASS' if hit else 'MISS'}  [{tier}, score {c.score}] {c.headline}")
        print(f"      items: {', '.join(i.id for i in c.items)}  verdict={c.verdict} importance={c.importance}")
        if c.tldr:
            print(f"      tldr: {c.tldr}")
        if c.action:
            print(f"      do:   {c.action}")
    print(f"\n{ok}/{len(merged)} stories landed where expected (Nimbus Cloud should be one story, noise should be dropped).")
    return 0
