#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
and validates it against the gate: UTF-8 text, 1 to 140 characters,
a single line, not only whitespace.
"""

import os
import sys

JOKE = (
    "I asked an electrician to fix my dad jokes -- "
    "he said they're not grounded, they just keep shocking everyone."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Validation: one line, 1-140 chars, not only whitespace.
    if "\n" in JOKE or "\r" in JOKE:
        print("FAIL: joke must be a single line", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("FAIL: joke must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(JOKE) <= 140:
        print(f"FAIL: joke is {len(JOKE)} chars, must be 1-140", file=sys.stderr)
        return 1
    words = JOKE.split()
    if not 5 <= len(words) <= 40:
        print(f"FAIL: joke is {len(words)} words, must be 5-40", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Read-back check: what landed on disk is exactly the joke.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != JOKE:
        print("FAIL: read-back mismatch", file=sys.stderr)
        return 1
    print(f"OK: wrote {len(JOKE)} chars to {path}")
    print(back)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
