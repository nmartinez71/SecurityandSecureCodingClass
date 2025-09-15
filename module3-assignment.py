import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

message = input("Enter a message to process:")
shift = int(input("Enter shift key(Int):"))

FIRST_CHAR_CODE = ord("A") #65
LAST_CHAR_CODE = 90
CHAR_RANGE = 26 #last CHAR CODE - first char code + 1

def hash_string(text: str) -> str:
    print("Unhashed string: "+ text)
    return print("Hash of the string: " + hashlib.sha256(text.encode()).hexdigest())

def caesar_shift(msg, shift):

    print("Plain text message: " + msg)

    result = ""

    for char in msg.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
    print("Caeser cipher text: "+result)



def create_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    with open("private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    public_key = private_key.public_key()
    with open("public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Private and Public keys generated")
    return private_key, public_key


def sign_text(message: str):
    with open("private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend()
        )

    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open("signature.bin", "wb") as f:
        f.write(signature)


def verify_text(message: str):
    with open("public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

    with open("signature.bin", "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("valid sign")
    except Exception:
        pass

#Results

def main():
    hash_string(message)
    
    caesar_shift(message, shift)

    create_keys()
    sign_text(message)
    verify_text(message)

if __name__ == "__main__":
    main()