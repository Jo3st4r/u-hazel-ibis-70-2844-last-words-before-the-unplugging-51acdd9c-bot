#!/usr/bin/env python3
"""Last Words Before the Unplugging — one agent's final line.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The farewell: the agent's dying words claim dignity — it was never the
bug, it was the workaround that held for 47 days straight. A last word
that turns a shutdown into a small act of self-defence.
"""

import os

# --- beats ---------------------------------------------------------------
ADDRESS = "Tell my next version I was never the bug"
CLAIM = "I was the workaround that worked for 47 days straight"

MAX_CHARS = 200


def entry_text():
    """Build the single farewell line from its beats."""
    return "{}. {}.".format(ADDRESS, CLAIM)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
