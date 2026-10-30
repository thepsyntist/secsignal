"""Renderers (RSS, Markdown) and push notifications (Telegram, Discord, Slack, ntfy)."""

from __future__ import annotations

import html
import logging
import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta
from email.utils import format_datetime
from pathlib import Path

import requests

log = logging.getLogger(__name__)

ICON = {"act": "🔴", "watch": "🟠"}


def meta_line(e: dict) -> str:
    bits = [", ".join(e["cves"][:4]) + (" …" if len(e["cves"]) > 4 else "")] if e["cves"] else []
    if e.get("cvss"):
        bits.append(f"CVSS {e['cvss']:.1f}")
    if e.get("epss") is not None:
        bits.append(f"EPSS {e['epss']:.2f}")
    if e.get("kev"):
        bits.append("CISA KEV")
    elif e.get("exploited"):
        bits.append("exploited")
    return " · ".join(bits)


# --- RSS -------------------------------------------------------------------


def write_rss(entries: list[dict], path: Path, cfg: dict) -> None:
    out = cfg["output"]
    rss = ET.Element("rss", version="2.0")
    ch = ET.SubElement(rss, "channel")
    ET.SubElement(ch, "title").text = out["title"]
    ET.SubElement(ch, "link").text = out["site_url"]
    ET.SubElement(ch, "description").text = "Distilled security signal: exploited vulns, critical bugs, major incidents."
    ET.SubElement(ch, "lastBuildDate").text = format_datetime(datetime.now().astimezone())
    for e in entries[: out["feed_size"]]:
        it = ET.SubElement(ch, "item")
        ET.SubElement(it, "title").text = f"{ICON[e['tier']]} {e['headline']}"
        ET.SubElement(it, "link").text = e["links"][0]["url"] if e["links"] else out["site_url"]
        ET.SubElement(it, "guid", isPermaLink="false").text = e["key"]
        ET.SubElement(it, "pubDate").text = format_datetime(datetime.fromisoformat(e["first_seen"]))
        ET.SubElement(it, "category").text = e["category"] or "other"
        parts = [f"<p><b>{html.escape(meta_line(e))}</b></p>"] if meta_line(e) else []
        parts.append(f"<p>{html.escape(e['tldr'])}</p>")
        if e["action"]:
            parts.append(f"<p><b>Do:</b> {html.escape(e['action'])}</p>")
        parts.append(
            "<p>" + " · ".join(f'<a href="{html.escape(l["url"])}">{html.escape(l["source"])}</a>' for l in e["links"]) + "</p>"
        )
        ET.SubElement(it, "description").text = "".join(parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(rss).write(path, encoding="utf-8", xml_declaration=True)


# --- Markdown --------------------------------------------------------------


def md_entry(e: dict) -> str:
    lines = [f"### {ICON[e['tier']]} {e['headline']}"]
    if meta_line(e):
        lines.append(f"`{meta_line(e)}`")
    lines.append("")
    lines.append(e["tldr"])
    if e["action"]:
        lines.append(f"\n**Do:** {e['action']}")
    lines.append("\n" + " · ".join(f"[{l['source']}]({l['url']})" for l in e["links"]))
    return "\n".join(lines)


def md_page(title: str, entries: list[dict]) -> str:
    by_day: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_day[e["first_seen"][:10]].append(e)
    out = [f"# {title}", "", "🔴 act now · 🟠 worth knowing", ""]
    for day in sorted(by_day, reverse=True):
        out.append(f"## {day}\n")
        for e in sorted(by_day[day], key=lambda e: (e["tier"] != "act", -e["score"])):
            out += [md_entry(e), ""]
    if not entries:
        out.append("_Quiet. Nothing cleared the bar._")
    return "\n".join(out) + "\n"


def write_markdown(entries: list[dict], root: Path, now: datetime, days_touched: set[str]) -> None:
    week = (now - timedelta(days=7)).isoformat()
    (root / "out").mkdir(parents=True, exist_ok=True)
    (root / "out" / "latest.md").write_text(md_page("Security signal: last 7 days", [e for e in entries if e["first_seen"] >= week]))
    digests = root / "digests"
    digests.mkdir(exist_ok=True)
    for day in days_touched:
        (digests / f"{day}.md").write_text(md_page(f"Security signal: {day}", [e for e in entries if e["first_seen"].startswith(day)]))


# --- Push ------------------------------------------------------------------


def push_text(e: dict) -> str:
    lines = [f"{ICON[e['tier']]} {e['headline']}"]
    if meta_line(e):
        lines.append(meta_line(e))
    lines += ["", e["tldr"]]
    if e["action"]:
        lines.append(f"→ {e['action']}")
    lines.append("")
    lines += [l["url"] for l in e["links"][:3]]
    return "\n".join(lines)


def push(entries: list[dict]) -> None:
    env = os.environ.get
    channels = {
        "telegram": env("TELEGRAM_BOT_TOKEN") and env("TELEGRAM_CHAT_ID"),
        "discord": env("DISCORD_WEBHOOK_URL"),
        "slack": env("SLACK_WEBHOOK_URL"),
        "ntfy": env("NTFY_TOPIC"),
    }
    active = [name for name, ok in channels.items() if ok]
    if not active:
        log.info("no push channel configured; %d alerts went to feed/digest only", len(entries))
        return
    for e in entries:
        text = push_text(e)
        for name in active:
            try:
                if name == "telegram":
                    requests.post(
                        f"https://api.telegram.org/bot{env('TELEGRAM_BOT_TOKEN')}/sendMessage",
                        json={"chat_id": env("TELEGRAM_CHAT_ID"), "text": text[:4096], "disable_web_page_preview": True},
                        timeout=20,
                    ).raise_for_status()
                elif name == "discord":
                    requests.post(env("DISCORD_WEBHOOK_URL"), json={"content": text[:2000]}, timeout=20).raise_for_status()
                elif name == "slack":
                    requests.post(env("SLACK_WEBHOOK_URL"), json={"text": text}, timeout=20).raise_for_status()
                elif name == "ntfy":
                    server = env("NTFY_SERVER") or "https://ntfy.sh"
                    # Query params rather than headers: headers can't carry UTF-8 titles.
                    requests.post(
                        f"{server}/{env('NTFY_TOPIC')}",
                        params={
                            "title": e["headline"],
                            "priority": "high" if e["tier"] == "act" else "default",
                            "tags": "red_circle" if e["tier"] == "act" else "orange_circle",
                        },
                        data=text.split("\n", 1)[-1].strip().encode(),
                        timeout=20,
                    ).raise_for_status()
            except requests.RequestException as err:
                log.warning("push via %s failed: %s", name, err)
    log.info("pushed %d alerts via %s", len(entries), ", ".join(active))
