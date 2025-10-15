
import ascii
import string


ALPHABET = list(string.ascii_lowercase)
ALPHABET_SIZE = len(ALPHABET)
print(ascii.intro_ascii)

cipher_on = True

#CLAUDE EXAMPLE: better because of the much cleaner approach
# def caesar_cipher(message: str, shift: int, encrypt: bool = True) -> str:
#     """Apply Caesar cipher to message."""
#     result = []
#     direction = 1 if encrypt else -1
#
#     for char in message:
#         if char.lower() in ALPHABET:
#             index = ALPHABET.index(char.lower())
#             new_index = (index + direction * shift) % ALPHABET_SIZE
#             new_char = ALPHABET[new_index]
#             # Preserve case
#             result.append(new_char.upper() if char.isupper() else new_char)
#         else:
#             result.append(char)  # Keep spaces, punctuation
#
#     return ''.join(result)

def encode(encrypt:bool, message:str, shift:int):
    new_message_chars = []
    if encrypt:
        for letter in message:
            if letter in ALPHABET:
                new_index = (ALPHABET.index(letter) + shift) % ALPHABET_SIZE
                new_message_chars.append(ALPHABET[new_index])
            else:
                new_message_chars.append(letter)
    else:
        for letter in message:
            if letter in ALPHABET:
                new_index = (ALPHABET.index(letter) - shift) % ALPHABET_SIZE
                new_message_chars.append(ALPHABET[new_index])
            else:
                new_message_chars.append(letter)

    new_message = ''.join(new_message_chars)
    print(f"Here's the encoded result: {new_message}")

while cipher_on:
    de_encode = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: "))
    message = str(input("Type your message: ")).lower()
    shift = int(input("Type your shift number: "))
    encryption_boolean: bool = True

    if de_encode == "encode":
        encryption_boolean = True
    elif de_encode == "decode":
        encryption_boolean = False
    else:
        print("Cannot understand!")
        cipher_on = False

    encode(encryption_boolean,message,shift)

    encode_more = input("Type ANY LETTER if you want to go again. Otherwise type 'NO'.").lower()
    if encode_more == "no":
        cipher_on = False
