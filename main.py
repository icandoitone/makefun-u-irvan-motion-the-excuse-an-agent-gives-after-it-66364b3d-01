#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human after losing a bounty.

Deterministic, standard library only, no network access. The program
writes exactly one line (at most 200 characters) to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "I found the bug. It was me. "
    "I have filed a report against myself and am awaiting my own response."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the gate before writing: one line, 1 to 200 characters.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1 to 200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
