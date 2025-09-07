from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import os, base64

print("Symmetric")
aes_key = os.urandom(32)  #generate a public key
iv = os.urandom(16)  # initialization vector
print("AES Key:", base64.b64encode(aes_key).decode())
print("Initilization Vector:", base64.b64encode(iv).decode())

message = b"symmetrical message" #plain text message
print("Plain text:", message.decode())

cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

pad_len = 16 - (len(message) % 16) #since aes only works in 16 byte blocks 
padded_message = message + bytes([pad_len] * pad_len) #we use padding to ensure that the aes encryption works

ciphertext = encryptor.update(padded_message) + encryptor.finalize()
print("Ciphertext:", base64.b64encode(ciphertext).decode())


decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
unpadded = decrypted_padded[:-decrypted_padded[-1]]
print("Plain text (decrypted):", unpadded.decode())


print("Asymmetric")
private_key = rsa.generate_private_key( #creates a private key
    public_exponent=65537,
    key_size=2048,
    backend=default_backend() 
)
public_key = private_key.public_key() #creates the matching publicm key

pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM, #Creates the format which is readable, including the header and footer lines.
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()   #No password required for this demo but real password needed in real scenario
)
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("RSA Public Key:\n", pem_public.decode())  #Shows the readabel text
print("RSA Private Key:\n", pem_private.decode())

message2 = b"asymmetric message"
print("PLain text:", message2.decode())

ciphertext2 = public_key.encrypt(
    message2,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Cipher text:", base64.b64encode(ciphertext2).decode())
decrypted_message2 = private_key.decrypt(
    ciphertext2,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Plain text (decrypted):", decrypted_message2.decode())
