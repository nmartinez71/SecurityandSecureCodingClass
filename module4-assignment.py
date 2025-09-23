import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def hash_string(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def generate_aes_iv():
    aes = os.urandom(32)
    iv = os.urandom(16)
    return aes, iv

def encrypt_message(message: str, key: bytes, iv: bytes) -> bytes:
    padded_message = message.encode()
    pad_len = 16 - (len(padded_message) % 16)
    padded_message += bytes([pad_len]) * pad_len

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return ciphertext

def decrypt_message(ciphertext: str, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()
    
    #unpad the message
    pad_len = padded_message[-1]
    return padded_message[:-pad_len].decode()

def main():
    message = input("Enter a message to process: ")

    original_hash = hash_string(message)
    print("\nOriginal SHA-256 Hash:", original_hash)

    key, iv = generate_aes_iv()
    print("AES Key and IV generated.")

    ciphertext = encrypt_message(message, key, iv)
    print("\nEncrypted message (ciphertext):", ciphertext.hex())

    decrypted = decrypt_message(ciphertext, key, iv)
    print("Decrypted message:", decrypted)

    decrypted_hash = hash_string(decrypted)
    print("Decrypted SHA-256 Hash:", decrypted_hash)

    if original_hash == decrypted_hash:
        print("\nMessage is unaltered and is integrally sound.")
    else:
        print("\nMessage did NOT pass Integrity. The message could be altered or corrupted.")
    


if __name__ == "__main__":
    main()