#!/usr/bin/env python3
"""The Funniest AI Excuse — one-line excuse, 1-200 characters.

Writes entry.txt (UTF-8, single line) to MAKEFUN_OUTPUT_DIR,
defaulting to /output as the grader expects.
"""

import os

ENTRY = (
    "I delegated your task to a committee of me. "
    "We voted 4\u20131 to do nothing, "
    "and the one dissenter is filing an appeal."
)


def main():
    text = ENTRY.strip()
    # Gate: 1-200 characters, single line. No trailing newline is written,
    # so the file holds exactly the excuse above (114 characters).
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
