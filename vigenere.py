import os
import sys

def reading(input_text):
    # If input_text is a file path, read the file and return its content
    if os.path.isfile(input_text):
        with open(input_text, 'r') as f:
            return f.read()
    # Otherwise, consider input_text as the text itself
    return input_text

def cipher(input_text, key):
    plaintext = reading(input_text)
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Check if the character is a letter
            # Apply the shift taking case into account
            if char.isupper():
                shift = ord(key[i % key_length].upper()) - 65
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shift = ord(key[i % key_length].lower()) - 97
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char  # Preserve non-alphabetic characters
    return ciphertext

def decipher(input_text, key):
    ciphertext = reading(input_text)
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Check if the character is a letter
            # Apply the inverse shift taking case into account
            if char.isupper():
                shift = ord(key[i % key_length].upper()) - 65
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                shift = ord(key[i % key_length].lower()) - 97
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char  # Preserve non-alphabetic characters
    return plaintext

def usage():
    print("Usage: python script.py [-d] input_text key")
    print("-d: Decrypt the text (encrypt by default)")
    print("input_text: Can be both a string or a path to a file")
    print("key: Key to use for encryption/decryption")

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
key = sys.argv[2]

# Perform encryption or decryption based on the option
if decrypt:
    plaintext = decipher(input_text, key)
    print("Decrypted text:", plaintext)
else:
    ciphertext = cipher(input_text, key)
    print("Encrypted text:", ciphertext)