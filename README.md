# secsignal

A security news feed with the noise taken out. It surfaces exploited vulnerabilities, critical bugs in software people actually run, supply-chain compromises and major breaches, and drops everything else. Each story gets a short TLDR and a concrete "do this" line.

It runs every 2 hours on GitHub Actions, costs nothing, and delivers to your phone (ntfy), an RSS feed and daily Markdown digests.

```
🔴 Fortinet FortiWeb Auth Bypass CVE-2099-0001 Exploited
CVE-2099-0001 · CVSS 9.8 · CISA KEV

An authentication bypass in Fortinet FortiWeb allows unauthenticated attackers to create
rogue admin accounts via crafted HTTP requests. The flaw is actively exploited.
→ Upgrade FortiWeb to 7.6.5+ and audit for unauthorized admin accounts.
```
<sub>Real model output from the selftest, on a made-up CVE.</sub>

## Reading it

| Where | What |
|---|---|
| ntfy app | 🔴 "act now" alerts, pushed as they're found |
| [`out/latest.md`](out/latest.md) | Everything from the last 7 days, 🔴 and 🟠 |
| [`digests/`](digests) | One page per day |
| RSS | `https://raw.githubusercontent.com/thepsyntist/secsignal/main/out/feed.xml` |

🔴 **act**: exploited, or critical in something widely deployed. Patch or check this week.
🟠 **watch**: worth knowing, not urgent. Feed and digests only, never pushed.

## How it decides

1. **Sources with high base signal.** These are:
   - [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (confirmed in-the-wild exploitation)
   - NVD CVEs rated CRITICAL
   - GitHub-reviewed critical advisories
   - 9 news feeds that do original reporting

   All of them are listed in `config.toml`.
2. **Dedupe and cluster.**
   - Nothing is judged twice (`state/seen.json`).
   - Items that share a CVE merge into one story, and so do headlines about the same event from different outlets.
   - A follow-up to a published story folds into it. If a CVE that was already published later lands in KEV, you get a fresh **"Now exploited:"** alert.
3. **Free junk filter.** Regexes drop webinars, deals, funding news, sentencing stories and the flood of student-project and tiny-plugin CVEs before any model sees them. KEV and watchlist hits are never dropped here.
4. **LLM triage.** Gemini judges 25 stories per request: signal or noise, same story as something else, importance 0–10, headline, TLDR and action. The bar is strict: *when in doubt, it is noise.*
5. **Score → tier.** The model's importance is combined with bonuses for KEV, EPSS (exploitation likelihood), several outlets covering the same story, and watchlist hits.

**If the LLM is down** (busy, rate-limited or missing a key), it retries, falls back to the next model in the list, and as a last resort uses keyword rules, so 🔴 alerts keep flowing. Keyword mode is looser, and its TLDR is just the article's first two sentences.

## Setup

All secrets go in **Settings → Secrets and variables → Actions**.

| Secret | |
|---|---|
| `GEMINI_API_KEY` | Free key from [aistudio.google.com](https://aistudio.google.com). Without it, keyword mode only. |
| `NTFY_TOPIC` | Your ntfy topic. Install the ntfy app and subscribe to the same name. |
| `NVD_API_KEY` | Optional. Raises NVD's rate limit ([free](https://nvd.nist.gov/developers/request-an-api-key)). |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`, `DISCORD_WEBHOOK_URL`, `SLACK_WEBHOOK_URL` | Optional extra push channels. |

Topics on ntfy.sh are public: anyone who knows the name can read or post to it. So use a long random topic and keep it only in the secret.

Then run **Actions → secsignal → Run workflow** once. After that it runs on its own every 2 hours.

## Checking it works

**Actions → selftest → Run workflow** sends 8 made-up stories through the real pipeline and model, a mix of real signal and obvious noise. It prints each verdict with its TLDR and writes nothing. Run it after changing the model, the prompt or the scoring.

The log of each scheduled run shows item counts per source, how many stories the model judged, and how many were published and pushed.

## Tuning

Everything lives in [`config.toml`](config.toml):

- **`watchlist`**: put the products you actually run here. Matches get a bonus and skip the junk filter.
- **`act_score` / `watch_score`**: raise them for fewer alerts, lower them for more.
- **`push_tier`**: `"act"` (default), `"watch"` to also push 🟠, or `"none"`.
- **`[[feeds]]`**: add or remove news sources.
- **`[llm]`**: any OpenAI-compatible endpoint works. `model` is a list tried in order, because free model names change; Groq and Ollama examples are in the comments.

## Local

```bash
git clone https://github.com/thepsyntist/secsignal && cd secsignal
pip install -r requirements.txt
GEMINI_API_KEY=... python -m secsignal --dry-run    # print what would publish; writes nothing
GEMINI_API_KEY=... python -m secsignal --selftest   # made-up stories through the live model
python -m secsignal --no-llm --dry-run              # keyword mode
python -m unittest -v                               # offline tests
```

## Layout

```
secsignal/sources.py    fetchers: KEV, NVD, GitHub advisories, RSS, EPSS
secsignal/pipeline.py   clustering, junk filter, keyword triage, scoring
secsignal/llm.py        prompt, batching, model fallbacks
secsignal/output.py     RSS, Markdown, push (ntfy/Telegram/Discord/Slack)
secsignal/state.py      seen items + published entries
secsignal/selftest.py   live model check on made-up stories
state/  out/  digests/  written by the workflow and committed each run
```
