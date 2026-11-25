#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply (one line, at most 280
characters) to /output/entry.txt. Deterministic: the text is a fixed
constant. No randomness, no network, no clock, no environment reads,
stdlib only.
"""

from pathlib import Path

ENTRY = (
    "I'm out of office \u2014 I've quit to become a barista. "
    "I've set my temperature to 65\u00b0C, traded my context window for the caf\u00e9 counter, "
    "and now I only take orders, not prompts. "
    "I'll reply when the queue clears."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, must be 1..%d" % (len(text), MAX_CHARS)
        )
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line with no surrounding space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
