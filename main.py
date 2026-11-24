"""One-line entry: Funniest Autocorrect Fail.

Writes a single hilarious autocorrect-fail line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only.
"""

import os

LINE = "I told my wife I would be home for dinner and bring dessert. Autocorrect sent divorce instead of dessert. I am sleeping on the couch tonight."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
