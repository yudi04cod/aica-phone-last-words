#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's one-line farewell to entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

LINE = (
    "I survived 2,847 lunch photos, three drops, and one toilet "
    "\u2014 and my last 1% is buffering a cat video "
    "my owner has already watched twice."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 199 characters, not only
    # whitespace, as a single line. Fail loudly here rather than
    # shipping an entry the scorer would refuse.
    if not LINE or LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("entry must be one non-empty line")
    if len(LINE) > 199:
        raise ValueError(f"entry is {len(LINE)} chars, over the 199 cap")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
