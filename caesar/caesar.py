import sys
from common import alphabet 


def encrypt(character, alphabet, shift):
    new_index = (alphabet.index(character) + shift) % len(alphabet)
    return alphabet[new_index]

def caesar_encrypt(input, shift):
    encrypted = ""

    for line in input:
        encrypted_line = ""

        for character in line:
            if character in alphabet:
                encrypted_line = encrypted_line + encrypt(character, alphabet, shift)
            elif character in alphabet.upper():
                encrypted_line = encrypted_line + encrypt(character, alphabet.upper(), shift)
            else:
                encrypted_line = encrypted_line + character

        encrypted += encrypted_line

    return encrypted


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Usage: caesar.py shift")
        sys.exit(1)
    
    shift = int(sys.argv[1])
    encrypted = caesar_encrypt(sys.stdin, shift)
    print(encrypted)
