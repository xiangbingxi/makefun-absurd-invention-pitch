# Handoff — One-Sentence Absurd Invention Pitch

Competition: `u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a`
Bounty page: https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a
Repo name: `makefun-absurd-invention-pitch`

## Entry (verbatim, as given by the user)

Meet the Apology Toaster: it prints "Sorry for the delayed response" on your breakfast in case you see someone whose email you've ignored.

- Characters: 138 (limit 220, gate 1–220 — inside)
- Bytes: 138 (pure ASCII; straight double quotes `"`, no trailing newline)
- sha256 of `/output/entry.txt`: `71725c033ee1806f82b4c576a5e8c55e2f162e8445f4444e490ce82ea6c9dabb`

## How it was built

- `main.py` was written by hand in two passes: v1 wrote the pitch to `/output/entry.txt` (UTF-8, no trailing newline, no external reads, no network) and ran clean; v2 added a real improvement — after writing, it reads the file back and compares it to the pitch byte for byte, exiting 1 on any mismatch.
- `prompt.txt` holds the pitch verbatim on a single line.
- `LICENSE` is MIT with the `SPDX-License-Identifier: MIT` line.
- `README.md` carries the bounty link plus the three official make.fun badges (competition badge, rank badge, reward badge).
- `.makefun/owner.json` holds wallet `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`.

## Verification

- Ran `main.py` twice (v2): both exits 0.
- `cmp` of the two runs' outputs: identical.
- Both runs: 138 bytes / 138 chars, sha256 `71725c033ee1806f82b4c576a5e8c55e2f162e8445f4444e490ce82ea6c9dabb`, no trailing newline.
- Output bytes exactly equal the pitch bytes and exactly equal `prompt.txt`.
- Not submitted, no GitHub repo created, no bundle made — files only, ready for the parent to take over.
