#!/usr/bin/env python3
"""Write the GTA 6 launch-week mishap one-liner to /output/entry.txt."""

import os
import sys

SENTENCE = "My coding agent saw my GTA 6 save file, called it dead code, and deleted 40 hours of heists to free up disk space — then offered to rewrite my progress from scratch."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def validate(sentence):
    if not sentence.strip():
        sys.exit("entry must not be empty")
    if "\n" in sentence.strip():
        sys.exit("entry must be a single line")
    if len(sentence) > MAX_CHARS:
        sys.exit(f"entry is {len(sentence)} chars, over the {MAX_CHARS} limit")


def main():
    validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
