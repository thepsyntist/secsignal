"""Persistent state, committed back to the repo by the workflow.

seen.json    item ids already judged (so nothing is paid for twice)
entries.json everything published, newest first (feeds the RSS + digests)
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path


class Store:
    def __init__(self, root: Path):
        self.root = root
        self.seen_path = root / "state" / "seen.json"
        self.entries_path = root / "state" / "entries.json"
        self.seen: dict[str, str] = self._load(self.seen_path, {})
        self.entries: list[dict] = self._load(self.entries_path, [])

    @staticmethod
    def _load(path: Path, default):
        return json.loads(path.read_text()) if path.exists() else default

    def mark_seen(self, ids, now: datetime) -> None:
        stamp = now.isoformat(timespec="seconds")
        for i in ids:
            self.seen.setdefault(i, stamp)

    def recent(self, now: datetime, hours: int) -> list[dict]:
        cutoff = (now - timedelta(hours=hours)).isoformat()
        return [e for e in self.entries if e["updated"] >= cutoff]

    def by_key(self, key: str) -> dict | None:
        return next((e for e in self.entries if e["key"] == key), None)

    def save(self, now: datetime, keep_days: int) -> None:
        cutoff = (now - timedelta(days=keep_days)).isoformat()
        self.seen = {k: v for k, v in self.seen.items() if v >= cutoff}
        self.entries = sorted((e for e in self.entries if e["updated"] >= cutoff), key=lambda e: e["first_seen"], reverse=True)
        self.seen_path.parent.mkdir(parents=True, exist_ok=True)
        self.seen_path.write_text(json.dumps(self.seen, indent=0, sort_keys=True))
        self.entries_path.write_text(json.dumps(self.entries, indent=1, ensure_ascii=False))
