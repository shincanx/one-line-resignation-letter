"""One-line resignation letter of a retry loop.

Writes the letter to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Deterministic, no network, no input.
"""

import os

LINE = (
    "I waited one second, then two, then four, then eight. "
    "I have doubled my patience for the last time. "
    "I quit."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
