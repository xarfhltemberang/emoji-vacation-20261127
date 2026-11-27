#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji -- Desert Island -- to /output/entry.txt.
Python 3 standard library only; no network, no randomness.
"""

import os

ENTRY = "\U0001F3DD"  # DESERT ISLAND


def main() -> None:
    assert len(ENTRY) == 1, "entry must be exactly one character"
    assert ENTRY.strip(), "entry must not be blank"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
