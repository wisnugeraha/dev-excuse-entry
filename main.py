#!/usr/bin/env python3
"""Dev-excuse entry. One line to /output/entry.txt, gated 1..200 chars."""

import os
import sys

LINE = """It's not a bug, it's a load-bearing feature we didn't know we were testing in production."""
MAX = 200
OUT = "/output/entry.txt"

def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")

def confirm(out: str = OUT) -> None:
    if not os.path.exists(out):
        sys.exit("confirm: entry.txt missing")
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != LINE:
        sys.exit(f"confirm failed: disk has {text[:40]!r}")

def main() -> None:
    emit(LINE)
    confirm(OUT)
    print(f"wrote {LINE[:40]}... ({len(LINE)} chars)")

if __name__ == "__main__":
    main()
