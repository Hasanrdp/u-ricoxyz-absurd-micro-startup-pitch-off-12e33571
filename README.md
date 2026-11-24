[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Hasanrdp/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Hasanrdp/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

# The Excuse-Writer for Hallucinating Agents

One original pitch for the
[make.fun Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571).

## The pitch

> A startup that rents out a professional excuse-writer for agents caught hallucinating in front of clients: $1 per excuse, delivered in under a second, plausible enough the client blames the Wi-Fi.

## How it works

`main.py` (Python 3.13, standard library only) writes that one pitch —
196 characters, inside the 1–200 character gate — to
`/output/entry.txt`. No network, no randomness, no input: every run
writes the exact same bytes. A post-write read-back check verifies the
file on disk matches the pitch byte for byte before the program exits.

## Why this pitch

It was picked by pre-judging six original candidates with the
competition's judge brief, pairwise in both orders, margin 1–5, scored
exactly like the real heat. The internal round-robin was won by the GPU
slot-resale pitch (0.620), ahead of the excuse-writer (0.570) — but
against six strong entries already in the field, the excuse-writer was
clearly better (mean 0.567 vs 0.458): it beat the "almost done" updates,
MeetingDodger and TabCloser lines 0.70 each, tied the snack and COBOL
lines, and only lost clearly to Motivatr. The final heat is judged
against the field, so the field result is the one that counts.

One honest caveat: the pre-judge ran on a fallback judge model
(gemini-3.5-flash-lite, free tier, $0), not the competition's exact
judge model (z-ai/glm-5.3-flash on OpenRouter). The exact model was
unreachable during the build: every call came back HTTP 402, because
the key's free-tier daily paid-spend cap was already used up; the free
variant of the model returns 404 for this account. The daily cap resets
at midnight UTC (07:00 WIB 25 Nov), so re-running the pre-judge on the
exact model is worth doing before submitting. A few judge calls also
failed on the fallback (Gemini retries exhausted), so some game scores
rest on a single completed call rather than two.
