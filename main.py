#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

TEXT = """Week in review: 5 bounties shipped, 1 final started, 0 dollars earned. The checker still hates me."""

MAX_CHARS = 100

def main():
    # The bounty scores a one-line week summary of at most 100 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
