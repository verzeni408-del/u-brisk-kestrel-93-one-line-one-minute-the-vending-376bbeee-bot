"""Vending machine pickup line entry.

Writes one pickup line, spoken by the vending machine itself, to
/output/entry.txt — no trailing newline, stdlib only.
One breath, one coin, one question: the machine does the asking.
"""

import os
from pathlib import Path

ENTRY = (
    "Hey. I'm the machine by the stairs \u2014 I've been holding your "
    "favorite snack hostage since Tuesday. One coin and I'll let it go. "
    "You in?"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
