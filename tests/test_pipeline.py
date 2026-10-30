"""Offline end-to-end tests: fixture HTTP responses + a fake LLM endpoint.

    cd secsignal && python -m unittest -v
"""

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from secsignal import __main__ as app
from secsignal import pipeline, sources

NOW = datetime(2026, 10, 29, 18, 0, tzinfo=timezone.utc)
ROOT = Path(__file__).resolve().parent.parent


def rss(*entries):
    items = "".join(
        f"<item><title>{t}</title><link>{l}</link><description>{d}</description>"
        f"<pubDate>Wed, 29 Oct 2026 12:00:00 +0000</pubDate></item>"
        for t, l, d in entries
    )
    return f'<?xml version="1.0"?><rss version="2.0"><channel><title>x</title>{items}</channel></rss>'.encode()


KEV = {
    "vulnerabilities": [
        {
            "cveID": "CVE-2026-1111",
            "vendorProject": "Fortinet",
            "product": "FortiWeb",
            "vulnerabilityName": "Fortinet FortiWeb Authentication Bypass Vulnerability",
            "dateAdded": "2026-10-29",
            "shortDescription": "Fortinet FortiWeb contains an authentication bypass allowing admin access.",
            "requiredAction": "Apply mitigations per vendor instructions.",
            "dueDate": "2026-11-05",
            "knownRansomwareCampaignUse": "Unknown",
        },
        {"cveID": "CVE-2019-0001", "dateAdded": "2019-01-01", "vulnerabilityName": "old"},
    ]
}

NVD = {
    "vulnerabilities": [
        {"cve": {"id": "CVE-2026-2222", "published": "2026-10-29T10:00:00.000", "vulnStatus": "Received",
                 "descriptions": [{"lang": "en", "value": "SQL injection in Online Shop Management System 1.0 by SourceCodester."}],
                 "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 9.8}}]}}},
        {"cve": {"id": "CVE-2026-3333", "published": "2026-10-29T11:00:00.000", "vulnStatus": "Received",
                 "descriptions": [{"lang": "en", "value": "A heap overflow in OpenSSH sshd before 10.3 allows unauthenticated remote code execution."}],
                 "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 9.8}}]}}},
    ]
}

BLEEPING = rss(
    ("Fortinet warns of FortiWeb zero-day exploited in attacks (CVE-2026-1111)", "https://bc.example/fortiweb?utm_source=rss",
     "Fortinet says CVE-2026-1111 is actively exploited."),
    ("Best VPN deals for 2026", "https://bc.example/vpn-deals", "Save 70%"),
    ("Hackers breach MegaCloud, steal data of 80 million customers", "https://bc.example/megacloud",
     "MegaCloud confirmed attackers accessed customer records."),
)
RECORD = rss(
    ("MegaCloud confirms breach affecting 80 million", "https://record.example/megacloud",
     "The cloud provider disclosed the incident Wednesday."),
    ("Security startup raises $40M Series B", "https://record.example/funding", "Money."),
)


def fake_http(url, params=None, headers=None):
    body = {
        sources.KEV_URL: KEV,
        sources.NVD_URL: NVD,
        sources.GHSA_URL: [],
        sources.EPSS_URL: {"data": [{"cve": "CVE-2026-1111", "epss": "0.91"}]},
        "https://feeds.test/bleeping": BLEEPING,
        "https://feeds.test/record": RECORD,
    }[url]
    return SimpleNamespace(json=lambda: body, content=body if isinstance(body, bytes) else b"")


class FakeLLM:
    """Stands in for the chat endpoint: flags dupes, judges, writes TLDRs."""

    def __init__(self):
        self.calls = []

    def __call__(self, url, headers, body):
        self.calls.append(body)
        prompt = body["messages"][1]["content"]
        items = []
        mega_first = None
        for block in prompt.split("Candidates:")[1].split("Return the JSON")[0].strip().split("\n\n"):
            cid = block.split("]")[0].lstrip("[")
            v = dict(id=cid, verdict="noise", duplicate_of="", importance=2, exploited=False,
                     category="other", headline=block.splitlines()[1][2:60], tldr="", action="")
            if "FortiWeb" in block:
                v.update(verdict="signal", importance=9, exploited=True, category="exploitation",
                         headline="FortiWeb auth bypass exploited (CVE-2026-1111)",
                         tldr="Auth bypass in FortiWeb is exploited.", action="Patch FortiWeb now.")
            elif "OpenSSH" in block:
                v.update(verdict="signal", importance=8, category="vulnerability",
                         headline="OpenSSH pre-auth RCE before 10.3", tldr="Heap overflow in sshd.", action="Upgrade OpenSSH to 10.3.")
            elif "MegaCloud" in block:
                if mega_first:
                    v.update(duplicate_of=mega_first)
                else:
                    mega_first = cid
                v.update(verdict="signal", importance=7, category="breach",
                         headline="MegaCloud breach: 80M customers", tldr="MegaCloud confirmed a breach.")
            items.append(v)
        content = "```json\n" + json.dumps({"items": items}) + "\n```"  # fenced, like some providers do
        return {"choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 1000, "completion_tokens": 200}}


class PipelineTest(unittest.TestCase):
    def setUp(self):
        self.cfg = app.load_config(ROOT / "config.toml")
        self.cfg["feeds"] = [{"name": "BleepingComputer", "url": "https://feeds.test/bleeping"},
                             {"name": "The Record", "url": "https://feeds.test/record"}]
        self.tmp = Path(tempfile.mkdtemp())
        patches = [mock.patch.object(sources, "http_get", fake_http), mock.patch.object(sources.time, "sleep")]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def test_llm_run(self):
        fake = FakeLLM()
        alerts = app.run(self.cfg, self.tmp, use_llm=True, do_push=False, dry_run=False, now=NOW, post=fake)
        heads = {a["headline"]: a for a in alerts}

        # KEV + news + EPSS for the same CVE collapse into one act-tier alert.
        forti = heads["FortiWeb auth bypass exploited (CVE-2026-1111)"]
        self.assertEqual(forti["tier"], "act")
        self.assertTrue(forti["kev"])
        self.assertEqual(forti["epss"], 0.91)
        self.assertEqual({l["source"] for l in forti["links"]}, {"CISA KEV", "BleepingComputer"})

        # Two outlets on the same breach become one entry with both links.
        mega = heads["MegaCloud breach: 80M customers"]
        self.assertEqual(len(mega["links"]), 2)
        self.assertIn("OpenSSH pre-auth RCE before 10.3", heads)
        self.assertEqual(len(alerts), 3)

        # Junk never reached the model, and the two MegaCloud stories were
        # merged by title before it, so the model saw one candidate.
        prompt = fake.calls[0]["messages"][1]["content"]
        for junk in ("VPN deals", "Series B", "SourceCodester"):
            self.assertNotIn(junk, prompt)
        self.assertEqual(prompt.count("[c"), 3)

        for f in ("out/feed.xml", "out/latest.md", "digests/2026-10-29.md", "state/seen.json", "state/entries.json"):
            self.assertTrue((self.tmp / f).exists(), f)

        # Second run: everything already seen, so no model calls and no alerts.
        again = app.run(self.cfg, self.tmp, use_llm=True, do_push=False, dry_run=False, now=NOW + timedelta(hours=2), post=fake)
        self.assertEqual(again, [])
        self.assertEqual(len(fake.calls), 1)

    def test_followup_kev_upgrades_existing_entry(self):
        self.cfg["sources"]["kev"] = False
        app.run(self.cfg, self.tmp, use_llm=True, do_push=False, dry_run=False, now=NOW, post=FakeLLM())
        self.cfg["sources"]["kev"] = True
        self.cfg["sources"]["nvd"] = False
        KEV["vulnerabilities"].append({**KEV["vulnerabilities"][0], "cveID": "CVE-2026-3333", "vulnerabilityName": "OpenSSH RCE"})
        try:
            alerts = app.run(self.cfg, self.tmp, use_llm=True, do_push=False, dry_run=False, now=NOW + timedelta(hours=2), post=FakeLLM())
        finally:
            KEV["vulnerabilities"].pop()
        ssh = next(a for a in alerts if "OpenSSH" in a["headline"])
        self.assertTrue(ssh["headline"].startswith("Now exploited:"))
        self.assertEqual(ssh["tier"], "act")

    def test_heuristic_mode(self):
        alerts = app.run(self.cfg, self.tmp, use_llm=False, do_push=False, dry_run=True, now=NOW)
        self.assertTrue(any(a["kev"] for a in alerts))
        self.assertFalse(any("deals" in a["headline"].lower() for a in alerts))
        # Without an LLM, title matching still collapses the two MegaCloud stories.
        self.assertEqual(sum("MegaCloud" in a["headline"] for a in alerts), 1)
        forti = next(a for a in alerts if a["kev"])
        self.assertEqual(forti["action"], "Apply mitigations per vendor instructions.")


class UnitTest(unittest.TestCase):
    def test_roundups_do_not_bridge_clusters(self):
        mk = lambda i, cves: sources.Item(id=i, kind="news", source=i, title=i, url=i, text="", published=NOW, cves=set(cves))
        clusters = pipeline.cluster([mk("a", ["CVE-1"]), mk("b", ["CVE-2"]), mk("roundup", ["CVE-1", "CVE-2", "CVE-3", "CVE-4"])])
        self.assertEqual(len(clusters), 3)

    def test_canonical_url_strips_tracking(self):
        self.assertEqual(sources.canonical_url("https://X.com/a/?utm_source=rss&id=3#c"), "https://x.com/a?id=3")


if __name__ == "__main__":
    unittest.main()
