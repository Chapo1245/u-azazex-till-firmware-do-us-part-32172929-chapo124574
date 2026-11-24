#!/usr/bin/env python3
"""Till Firmware Do Us Part - make.fun entry.

Writes one robot wedding vow (a single sentence, under 200 characters)
to /output/entry.txt. Deterministic: the same bytes on every run.
Standard library only.
"""

import os

VOW = (
    "I vow to love you through every firmware update, "
    "even the ones that brick me, "
    "until my last battery dies at your side."
)
# 118 characters, one sentence, no trailing newline: the gate counts
# 1-200 characters and the entry is exactly this line.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
