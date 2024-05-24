import os
import sys

def read_input_text(input_text):
    # If input_text is a file path, read the file and return its content
    if os.path.isfile(input_text):
        # file deepcode ignore PT: <please specify a reason of ignoring this>
        with open(input_text, 'r') as f:
            return f.read()
    # Otherwise, consider input_text as the text itself
    return input_text

def caesar_cipher(input_text, shift):
    plaintext = read_input_text(input_text)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Apply the shift taking case into account
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char  # Preserve non-alphabetic characters
    return ciphertext

def caesar_decipher(input_text, shift):
    ciphertext = read_input_text(input_text)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Apply the inverse shift taking case into account
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char  # Preserve non-alphabetic characters
    return plaintext

def usage():
    print("Usage: python script.py [-d] input_text shift")
    print("-d: Decrypt the text (encrypt by default)")
    print("input_text: Can be both a string or a path to a file")
    print("shift: shift to apply to input_text")

# Check command line arguments
if len(sys.argv) < 3:
    usage()
    sys.exit(1)

# Determine if decrypt option is provided
decrypt = False
if len(sys.argv) > 3 and sys.argv[1] == "-d":
    decrypt = True
    del sys.argv[1]  # Remove the decrypt option from the argument list

# Get the remaining arguments
input_text = sys.argv[1]
shift = int(sys.argv[2])

# Perform encryption or decryption based on the option
if decrypt:
    plaintext = caesar_decipher(input_text, shift)
    print("Decrypted text:", plaintext)
else:
    ciphertext = caesar_cipher(input_text, shift)
    print("Encrypted text:", ciphertext)
