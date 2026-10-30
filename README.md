# secsignal

A security news feed that only lets serious items through: actively exploited vulns, critical bugs in software people actually run, supply-chain compromises and major breaches. Each item gets a two-sentence TLDR and a "do this" line. Runs every 2 hours on GitHub Actions and writes an RSS feed, Markdown digests and (optionally) phone/chat alerts.

```
🔴 FortiWeb auth bypass exploited (CVE-2026-1111)
CVE-2026-1111 · EPSS 0.91 · CISA KEV

Unauthenticated attackers can create admin accounts on FortiWeb 7.x; CISA confirms exploitation.
→ Upgrade FortiWeb to 7.4.8+ and audit for unknown admin accounts.
```

## How it filters

1. **Sources with high base signal.** CISA KEV (confirmed exploitation), NVD CRITICAL CVEs, GitHub-reviewed critical advisories, and a short list of original-reporting news feeds (`config.toml`).
2. **Dedupe and cluster.** Items are never judged twice (`state/seen.json`). Items sharing a CVE merge into one story, and so do headlines about the same thing from different outlets. Follow-ups to a story that was already published fold into it. If a published CVE later lands in KEV, you get a "Now exploited:" alert.
3. **Free junk filter.** Regexes drop webinars, deals, funding, sentencing and the long tail of student-project and tiny-plugin CVEs before the LLM sees them. Watchlist and KEV items are exempt.
4. **One batched LLM call** per 15 candidates does triage, dedupe, headline, TLDR and action together. The prompt sets a strict bar: "when in doubt, it is noise".
5. **Score → tier.** LLM importance plus KEV, EPSS, multi-outlet corroboration and watchlist bonuses. 🔴 `act` is pushed; 🟠 `watch` only goes to the feed and digest.

## Cost: free

The LLM step uses Gemini's free tier through its OpenAI-compatible endpoint: get a key at [aistudio.google.com](https://aistudio.google.com) and store it as the `GEMINI_API_KEY` repo secret. A run needs a couple of requests (25 candidates each), well inside the free limits. On the free tier Google may use inputs to improve its models; here that's public news headlines only.

`model` is a list tried in order, because free model names change; the first one that answers is used. `[llm]` accepts any OpenAI-compatible endpoint (Groq and a local Ollama are in the comments). If the LLM is unavailable, rate-limited or has no key, the keyword rules take over so alerts keep flowing. They're looser, though, and the TLDR is just the article's first two sentences.

## Setup

Add the `GEMINI_API_KEY` secret, then trigger **Actions → secsignal → Run workflow** once. After that it runs every 2 hours.

Optional secrets (**Settings → Secrets and variables → Actions**):

| Secret | |
|---|---|
| `NTFY_TOPIC` | ntfy topic for phone push: install the ntfy app and subscribe to the same topic |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Telegram push |
| `DISCORD_WEBHOOK_URL` / `SLACK_WEBHOOK_URL` | chat push |
| `NVD_API_KEY` | higher NVD rate limit ([free](https://nvd.nist.gov/developers/request-an-api-key)) |

Reading it: `out/latest.md` (last 7 days), `digests/YYYY-MM-DD.md`, or subscribe in any RSS reader: `https://raw.githubusercontent.com/thepsyntist/secsignal/main/out/feed.xml`.

## Local

```bash
git clone https://github.com/thepsyntist/secsignal && cd secsignal
pip install -r requirements.txt
GEMINI_API_KEY=... python -m secsignal --dry-run   # print what would publish; writes nothing
python -m secsignal --no-llm --dry-run # free mode
python -m unittest -v                  # offline tests with fixtures
```

## Tuning

Everything lives in `config.toml`. The most useful knobs are `watchlist` (put your actual stack here), `act_score`/`watch_score`, `push_tier` and the feed list.
