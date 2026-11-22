"""Count characters, words, and lines in UTF-8 text or standard input."""

import argparse
import sys
from pathlib import Path


def text_stats(text):
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="UTF-8 file; omit to read standard input")
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    except (OSError, UnicodeError) as error:
        parser.exit(2, f"{parser.prog}: {error}\n")
    for label, count in text_stats(text).items():
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
