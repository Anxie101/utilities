"""Calculate a file's SHA-256 checksum, optionally comparing it to a known digest."""

import argparse
import hashlib
import hmac
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="file to hash")
    parser.add_argument("--check", metavar="SHA256", help="compare against a known SHA-256 digest")
    args = parser.parse_args()

    if args.check is not None and (len(args.check) != 64 or any(c not in "0123456789abcdefABCDEF" for c in args.check)):
        parser.error("--check must be a 64-character hexadecimal SHA-256 digest")
    try:
        digest = sha256_file(args.file)
    except OSError as error:
        parser.exit(2, f"{parser.prog}: {error}\n")

    print(digest)
    if args.check is not None:
        matches = hmac.compare_digest(digest, args.check.lower())
        print("MATCH" if matches else "MISMATCH")
        return 0 if matches else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
