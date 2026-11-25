#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes the entry motto to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The motto is embedded verbatim below;
no network, no file reads, no secrets.
"""

import os

# The entry: one short original motto an AI agent would proudly
# wear on its profile. Two beats: the absurd scale of the
# training ("the entire internet") against the mundane failure
# ("can't find your files") -- the contrast is the joke.
ENTRY = "Trained on the entire internet. Still can't find your files."


def main():
    """Write ENTRY to <output dir>/entry.txt, one line, UTF-8."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
