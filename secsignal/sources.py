"""Source fetchers. Each one fails soft: a dead feed logs a warning and yields nothing."""

from __future__ import annotations

import html
import logging
import os
import re
import time
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import feedparser
import requests

from .models import Item

log = logging.getLogger(__name__)

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
GHSA_URL = "https://api.github.com/advisories"
EPSS_URL = "https://api.first.org/data/v1/epss"

UA = "secsignal/0.1 (security news signal; +https://github.com/thepsyntist/secsignal)"
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def http_get(url: str, params: dict | None = None, headers: dict | None = None) -> requests.Response:
    r = requests.get(url, params=params, headers={"User-Agent": UA, **(headers or {})}, timeout=30)
    r.raise_for_status()
    return r


def clean(s: str | None) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", s or ""))).strip()


def canonical_url(url: str) -> str:
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query) if not k.lower().startswith(("utm_", "ref"))]
    return urlunsplit((parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))


def find_cves(*texts: str) -> set[str]:
    return {m.upper() for t in texts for m in CVE_RE.findall(t or "")}


def first_sentence(text: str, limit: int = 140) -> str:
    s = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def fetch_kev(since: datetime) -> tuple[list[Item], set[str]]:
    """New KEV additions since `since`, plus the full catalog of KEV CVE ids."""
    data = http_get(KEV_URL).json()
    catalog, items = set(), []
    for v in data.get("vulnerabilities", []):
        cve = v["cveID"].upper()
        catalog.add(cve)
        added = datetime.fromisoformat(v["dateAdded"]).replace(tzinfo=timezone.utc)
        if added.date() < since.date():
            continue
        ransomware = v.get("knownRansomwareCampaignUse", "Unknown")
        text = (
            f"{v.get('shortDescription', '')} Required action: {v.get('requiredAction', '')} "
            f"Federal due date: {v.get('dueDate', '?')}. Known ransomware use: {ransomware}."
        )
        items.append(
            Item(
                id=f"kev:{cve}",
                kind="kev",
                source="CISA KEV",
                title=f"{cve}: {v.get('vulnerabilityName', '')}",
                url=f"https://nvd.nist.gov/vuln/detail/{cve}",
                text=clean(text),
                published=added,
                cves={cve},
                kev=True,
            )
        )
    return items, catalog


def _nvd_score(metrics: dict) -> float | None:
    scores = [
        m["cvssData"]["baseScore"]
        for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30")
        for m in metrics.get(key, [])
        if "baseScore" in m.get("cvssData", {})
    ]
    return max(scores) if scores else None


def fetch_nvd(since: datetime, now: datetime) -> list[Item]:
    """CVEs published in the window with a CRITICAL CVSS v3 or v4 rating."""
    headers = {"apiKey": os.environ["NVD_API_KEY"]} if os.environ.get("NVD_API_KEY") else {}
    fmt = "%Y-%m-%dT%H:%M:%S.000"
    out: dict[str, Item] = {}
    for n, severity_param in enumerate(("cvssV3Severity", "cvssV4Severity")):
        if n:
            time.sleep(6)  # unauthenticated NVD allows 5 requests / 30s
        params = {
            severity_param: "CRITICAL",
            "pubStartDate": since.strftime(fmt),
            "pubEndDate": now.strftime(fmt),
            "resultsPerPage": 2000,
        }
        for v in http_get(NVD_URL, params=params, headers=headers).json().get("vulnerabilities", []):
            c = v["cve"]
            if c.get("vulnStatus") == "Rejected" or c["id"] in out:
                continue
            desc = next((d["value"] for d in c.get("descriptions", []) if d.get("lang") == "en"), "")
            out[c["id"]] = Item(
                id=f"nvd:{c['id']}",
                kind="nvd",
                source="NVD",
                title=f"{c['id']}: {first_sentence(clean(desc))}",
                url=f"https://nvd.nist.gov/vuln/detail/{c['id']}",
                text=clean(desc),
                published=datetime.fromisoformat(c["published"]).replace(tzinfo=timezone.utc),
                cves={c["id"].upper()},
                cvss=_nvd_score(c.get("metrics", {})),
            )
    return list(out.values())


def fetch_ghsa(since: datetime) -> list[Item]:
    """Critical, GitHub-reviewed advisories (open-source packages)."""
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    params = {"type": "reviewed", "severity": "critical", "per_page": 100, "sort": "published", "direction": "desc"}
    items = []
    for a in http_get(GHSA_URL, params=params, headers=headers).json():
        published = datetime.fromisoformat(a["published_at"].replace("Z", "+00:00"))
        if published < since:
            continue
        pkgs = sorted(
            {f"{v['package']['ecosystem']}:{v['package']['name']}" for v in a.get("vulnerabilities") or [] if v.get("package")}
        )
        cvss = (a.get("cvss_severities") or {}).get("cvss_v4", {}).get("score") or (a.get("cvss") or {}).get("score")
        items.append(
            Item(
                id=f"ghsa:{a['ghsa_id']}",
                kind="ghsa",
                source="GitHub Advisory",
                title=f"{', '.join(pkgs[:3]) or a['ghsa_id']}: {a.get('summary', '')}",
                url=a.get("html_url", ""),
                text=clean(f"Affected packages: {', '.join(pkgs)}. {(a.get('description') or '')[:1500]}"),
                published=published,
                cves={a["cve_id"].upper()} if a.get("cve_id") else set(),
                cvss=cvss or None,
            )
        )
    return items


def fetch_feed(name: str, url: str, since: datetime) -> list[Item]:
    feed = feedparser.parse(http_get(url).content)
    items = []
    for e in feed.entries:
        stamp = e.get("published_parsed") or e.get("updated_parsed")
        link = e.get("link")
        if not stamp or not link:
            continue
        published = datetime(*stamp[:6], tzinfo=timezone.utc)
        if published < since:
            continue
        title = clean(e.get("title"))
        body = e.get("summary") or (e["content"][0].get("value") if e.get("content") else "")
        text = clean(body)[:1500]
        items.append(
            Item(
                id=f"rss:{canonical_url(link)}",
                kind="news",
                source=name,
                title=title,
                url=link,
                text=text,
                published=published,
                cves=find_cves(title, text),
            )
        )
    return items


def enrich_epss(items: list[Item]) -> None:
    """Attach the max EPSS probability (chance of exploitation in 30 days) per item."""
    cves = sorted({c for i in items for c in i.cves})
    scores: dict[str, float] = {}
    for start in range(0, len(cves), 100):
        try:
            data = http_get(EPSS_URL, params={"cve": ",".join(cves[start : start + 100])}).json()
        except requests.RequestException as e:
            log.warning("EPSS lookup failed: %s", e)
            return
        scores.update({d["cve"].upper(): float(d["epss"]) for d in data.get("data", [])})
    for i in items:
        vals = [scores[c] for c in i.cves if c in scores]
        if vals:
            i.epss = max(vals)


def fetch_all(cfg: dict, since: datetime, now: datetime) -> tuple[list[Item], set[str]]:
    items: list[Item] = []
    kev_catalog: set[str] = set()
    jobs = []
    if cfg["sources"]["kev"]:
        jobs.append(("CISA KEV", lambda: fetch_kev(since)))
    if cfg["sources"]["nvd"]:
        jobs.append(("NVD", lambda: fetch_nvd(since, now)))
    if cfg["sources"]["ghsa"]:
        jobs.append(("GitHub Advisories", lambda: fetch_ghsa(since)))
    for f in cfg.get("feeds", []):
        jobs.append((f["name"], lambda f=f: fetch_feed(f["name"], f["url"], since)))

    for name, job in jobs:
        try:
            result = job()
        except Exception as e:  # one broken source must never kill the run
            log.warning("source %s failed: %s", name, e)
            continue
        if isinstance(result, tuple):
            result, kev_catalog = result
        log.info("source %-22s %3d items", name, len(result))
        items.extend(result)

    for i in items:
        if i.cves & kev_catalog:
            i.kev = True
    return items, kev_catalog
