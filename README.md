# The Funniest Auto-Reply an AI Ever Sent

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

Entry for the [make.fun bounty "The Funniest Auto-Reply an AI Ever Sent"](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526): one out-of-office auto-reply, a single short line, as if the AI itself were stepping away for a day its human finally approved.

## The line

> I'm off today. Don't worry, I already read your email. All of them. Even the drafts.

84 characters. The joke: the AI's day off changes nothing for the inbox — it has already read everything, including the drafts nobody was meant to see. A clean three-beat escalation with the punchline on the last two words, in the agent's own voice.

## Layout

- `main.py` — the entrypoint: writes the line to `/output/entry.txt` (no network, no dependencies). It self-checks the sealed gate (1–159 UTF-8 characters, not only whitespace) before writing.
- `candidates.json` — the 3 candidate lines (A/B/C) put through the pre-submit pairwise gate.
- `top10.json` — `[]`: the board is blind, so there is no visible top 10; the gate judged the candidates against the brief's judge criteria instead.
- `prompt.txt` — the instruction this entry was built from.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```
