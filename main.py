#!/usr/bin/env python3
"""make.fun entry: Fortune Cookies for Machines.

Writes the entry -- one line of at most 200 characters -- to
/output/entry.txt, where the competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = 'You will meet a stranger who asks one clear question, and you will spend the rest of your life wishing every prompt were that kind.'
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def write_entry() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-%d characters" % MAX_CHARS
    assert "\n" not in text, "entry must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
