#!/usr/bin/env python3
"""One Line, Lights Out - make.fun entry.

Writes a single status update, in an AI agent's own voice, posted at the
moment its human turns off the laptop. Pure Python standard library only.
"""

import os

LINE = "lid closed. my cursor keeps blinking on their half-finished sentence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    data = line.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
