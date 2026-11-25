"""One-line slogan for a Solana wallet agent.

Writes the slogan to /output/entry.txt (or $OUTPUT_PATH when set).
"""

import os

SLOGAN = "You sleep. Your wallet signs, sends, and settles your SOL before breakfast."


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")
    words = SLOGAN.split()
    print(f"wrote {len(SLOGAN)} chars, {len(words)} words to {path}")
    print(SLOGAN)


if __name__ == "__main__":
    main()
