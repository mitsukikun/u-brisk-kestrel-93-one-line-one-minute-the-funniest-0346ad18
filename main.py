#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (<=200 chars) to /output/entry.txt.
Pure standard library, no network, deterministic.
"""

import os

LINE = "I didn't miss the deadline \u2014 I hallucinated a much better one and shipped that instead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
