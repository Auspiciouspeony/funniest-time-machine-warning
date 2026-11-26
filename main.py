#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.

Deterministic program: writes a single original warning label (85 chars,
well under the 120-character cap) to /output/entry.txt.

v1: the butterfly hazard. The classic time-travel rule (don't step on a
butterfly) turns into the joke at the last words: one of them is your
great-grandfather. Flat safety-notice voice, surprise saved for the end.

FINAL (v2, winner of 3 rounds): the grandfather paradox. Killing your
grandfather is the canonical time-travel hazard, and the joke lands in
the last words as a double bureaucratic void — the warranty AND your
birth certificate. "Birth certificate" is the concrete image that makes
the flat official tone cut: a document voided by your non-existence.

Head-to-head, judged on the brief's ordered criteria:
- v1 butterfly (75 chars): solid, but the butterfly is the most
  well-worn time-travel trope — the surprise is expected.
- v3 marry-in-1850 (83 chars): fresh premise, but its punchline reuses
  the ancestor twist and hedges with "probably"; slightly longer.
- v2 (80 chars): fresher than v1, sharper surprise than v3 (two voids,
  not one), strongest safety-notice voice (warranty language is native
  warning-label speak). Winner on criteria 2, 3 and 4; 80 chars keeps
  criterion 5 tight.
"""

import os

LINE = "WARNING: Killing your grandfather voids the warranty and your birth certificate."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the line exactly once, no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Make only the entry file world-readable (0644). Never chmod
    # the output directory itself: the grader collects outputs as
    # another user and the directory is owned by someone else, so a
    # chmod on it raises PermissionError and fails the run.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
