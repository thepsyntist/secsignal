from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

# Order used when picking which item "leads" a cluster: readable news first,
# then the authoritative advisories.
KIND_ORDER = {"news": 0, "kev": 1, "ghsa": 2, "nvd": 3}


@dataclass
class Item:
    id: str  # stable dedupe key, e.g. "kev:CVE-2026-1234", "rss:<url>"
    kind: str  # kev | nvd | ghsa | news
    source: str  # display name
    title: str
    url: str
    text: str
    published: datetime
    cves: set[str] = field(default_factory=set)
    cvss: float | None = None
    epss: float | None = None
    kev: bool = False


@dataclass
class Cluster:
    """One story: every item that talks about the same vulnerability/incident."""

    items: list[Item]
    cid: str = ""
    watch_hit: str = ""
    # Filled in by triage.
    verdict: str = ""
    duplicate_of: str = ""
    importance: int = 0
    exploited: bool = False
    category: str = ""
    headline: str = ""
    tldr: str = ""
    action: str = ""
    score: int = 0

    def ordered(self) -> list[Item]:
        return sorted(self.items, key=lambda i: (KIND_ORDER[i.kind], i.published))

    @property
    def cves(self) -> list[str]:
        return sorted(set().union(*(i.cves for i in self.items)))

    @property
    def kev(self) -> bool:
        return any(i.kev for i in self.items)

    @property
    def cvss(self) -> float | None:
        vals = [i.cvss for i in self.items if i.cvss is not None]
        return max(vals) if vals else None

    @property
    def epss(self) -> float | None:
        vals = [i.epss for i in self.items if i.epss is not None]
        return max(vals) if vals else None

    @property
    def news_sources(self) -> set[str]:
        return {i.source for i in self.items if i.kind == "news"}

    @property
    def key(self) -> str:
        return min(i.id for i in self.items)

    def links(self) -> list[dict]:
        seen, out = set(), []
        for i in self.ordered():
            if i.url and i.url not in seen:
                seen.add(i.url)
                out.append({"source": i.source, "url": i.url})
        return out
