"""Entry v2: a vending machine speaks its own pickup line.

The machine has been broken for months and watched people give up on it.
It has one minute of attention, so it spends it on the one person who still
looks at it like it might work, turning months of humiliation into a compliment.
"""

from pathlib import Path

ENTRY = "Row C4 stuck since March. It ate a kid's last dollar Tuesday, and you're the first person since who looked at me like I could still deliver."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
