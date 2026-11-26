# Apology Toaster — One-Sentence Absurd Invention Pitch

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/xiangbingxi/makefun-absurd-invention-pitch/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/xiangbingxi/makefun-absurd-invention-pitch/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a) bounty on make.fun.

## The pitch

> Meet the Apology Toaster: it prints "Sorry for the delayed response" on your breakfast in case you see someone whose email you've ignored.

One sentence, 138 characters — inside the 220-character limit.

## How it works

Run `main.py` (Python 3, no dependencies, no network, reads no external files). It writes the pitch exactly as written, UTF-8 with no trailing newline, to `/output/entry.txt`, then reads the file back and verifies it matches the pitch byte for byte, exiting non-zero on any mismatch.

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `prompt.txt` — the pitch, one line, verbatim
- `LICENSE` — MIT
- `HANDOFF.md` — build notes and verification results
