# utilities

All Scripts in here are small utilities made for educationnal purpose and do not aim to be used in real envirronment.

# Caesar.py
Small script to try the Caesar algorithm on strings or files.

Usage: python script.py [-d] input_text shift
       -d: Decrypt the text (encrypt by default)
       input_text: Can be both a string or a path to a file
       shift: shift to apply to input_text


# Vigerere.py
Small script to try the Vigenere algorithm on strings or files.

Usage: python script.py [-d] input_text key
       -d: Decrypt the text (encrypt by default)
       input_text: Can be both a string or a path to a file
       key: Key to use for encryption/decryption

# File checksum

Calculate a file's SHA-256 digest, or compare it with a known digest:

```sh
python file_checksum.py path/to/file
python file_checksum.py path/to/file --check EXPECTED_SHA256_DIGEST
```

The comparison returns exit code 0 for a match, 1 for a mismatch, and 2 for an error. A checksum detects changes only when the expected digest comes from a trusted source.

# Text statistics

Count characters, whitespace-separated words, and lines in a UTF-8 file or standard input:

```sh
python text_stats.py path/to/file.txt
python text_stats.py < path/to/file.txt
```

Characters include whitespace and line breaks. Lines are counted using Python's `splitlines()`: an empty input has zero lines, and a final line break does not add an extra line.
