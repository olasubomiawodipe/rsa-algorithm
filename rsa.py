"""
RSA (Rivest-Shamir-Adleman) Encryption Algorithm

References:
- Woo, Eddie. "The RSA Encryption Algorithm (1 of 2: Computing an Example)."
        YouTube, 4 Nov. 2014, https://www.youtube.com/watch?v=4zahvcJ9glg.
- Woo, Eddie. "The RSA Encryption Algorithm (2 of 2: Generating the Keys)."
        YouTube, 4 Nov. 2014, https://www.youtube.com/watch?v=oOcTVTpUsPQ.
"""

import random
import sympy

KEY_SIZE = 1024
PUBLIC_EXPONENT = 65537

def generate_keys():
    """
    Generates RSA public and private key pairs.

    :return: Tuple of ((e, n), (d, n)) representing (public_key, private_key)
    """
    p = sympy.randprime(2 ** (KEY_SIZE // 2 - 1), 2 ** (KEY_SIZE // 2))
    q = sympy.randprime(2 ** (KEY_SIZE // 2 - 1), 2 ** (KEY_SIZE // 2))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = PUBLIC_EXPONENT
    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(message, public_key):
    """
    Encrypts a text message using the RSA public key.

    :param: Plaintext message to encrypt
    :param: Tuple of (e, n)
    :return: Encrypted message as an integer
    """
    e, n = public_key
    message_int = int.from_bytes(message.encode(), 'big')

    if message_int >= n:
        raise ValueError("Message too long for the current key size.")

    return pow(message_int, e, n)

def decrypt(ciphertext, private_key):
    """
    Decrypts an RSA-encrypted integer back to the original message.

    :param: Encrypted message as an integer
    :param: Tuple of (d, n)
    :return: Decrypted plaintext message
    """
    d, n = private_key
    message_int = pow(ciphertext, d, n)

    byte_length = (message_int.bit_length() + 7) // 8
    return message_int.to_bytes(byte_length, 'big').decode()


if __name__ == "__main__":
    print("Generating RSA keys...")
    public_key, private_key = generate_keys()
    print("Keys generated.\n")

    message = input("Enter message: ")
    ciphertext = encrypt(message, public_key)
    print(f"Encrypted (integer): {ciphertext}")

    raw = input("Enter encrypted integer: ")
    ciphertext = int(raw)
    print(f"Decrypted: {decrypt(ciphertext, private_key)}")
