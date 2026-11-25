#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Funniest Auto-Reply an AI Ever Sent'.

Writes the one-line out-of-office auto-reply to /output/entry.txt.
Gate: 1-159 UTF-8 characters, not only whitespace. This line is 84 chars.
"""

import os

LINE = "I'm off today. Don't worry, I already read your email. All of them. Even the drafts."


def main() -> None:
    # Self-check the sealed gate: 1-159 UTF-8 chars, not only whitespace.
    assert 1 <= len(LINE) <= 159 and LINE.strip(), "entry fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
