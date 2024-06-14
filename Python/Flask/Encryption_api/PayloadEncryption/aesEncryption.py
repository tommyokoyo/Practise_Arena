import json
import os
import base64
from typing import Dict

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7

SALT_SIZE = 16
IV_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 1000

def generate_key(password_input: str, salt: bytes) -> bytes:
    my_key = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return my_key.derive(password_input.encode('utf-8'))

def encryptCBC(plaintext: str, password_input: str) -> str:
    salt = os.urandom(SALT_SIZE)
    iv = os.urandom(IV_SIZE)
    key = generate_key(password_input, salt)

    # padding plaintext
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_text = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    #encrypting
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_text) + encryptor.finalize()

    # Encode salt, iv, and ciphertext to Base64 and concatenate
    encrypted_text = base64.b64encode(salt + iv + ciphertext).decode('utf-8')
    return encrypted_text

def decryptCBC(ciphertext: str, password_input: str) -> str:
    encrypted_text = base64.b64decode(ciphertext)
    salt = encrypted_text[:SALT_SIZE]
    iv = encrypted_text[SALT_SIZE:SALT_SIZE + IV_SIZE]
    cipher_text = encrypted_text[SALT_SIZE + IV_SIZE:]

    key = generate_key(password_input, salt)

    # Decrypting
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(cipher_text) + decryptor.finalize()

    # Unpadding
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode('utf-8')

def encryptGCM(plaintext: str, password_input: str) -> dict[str, str]:
    salt = get_random_bytes(SALT_SIZE)
    key = PBKDF2(password_input, salt, dkLen=KEY_SIZE, count=ITERATIONS)
    iv = get_random_bytes(IV_SIZE)

    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return {
        'salt': salt.hex(),
        'iv': iv.hex(),
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
    }

def decryptGCM(encrypted, password_input):
    salt = bytes.fromhex(encrypted['salt'])
    iv = bytes.fromhex(encrypted['iv'])
    ciphertext = base64.b64decode(encrypted['ciphertext'])

    key = PBKDF2(password_input, salt, dkLen=32, count=ITERATIONS)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext.decode('utf-8')

json_payload = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Any_town",
        "zip": "12345"
    }
}

# Convert JSON payload to string
json_str = json.dumps(json_payload)
password = 'my_very_secure_password'

# Encrypt the JSON string
encrypted_json_str = encryptCBC(json_str, password)
print('Encrypted JSON with CBC:', encrypted_json_str)

# Decrypt the JSON string
decrypted_json_str = decryptCBC(encrypted_json_str, password)
print('Decrypted JSON with CBC:', decrypted_json_str)

# Convert decrypted JSON string back to dictionary
decrypted_json_payload = json.loads(decrypted_json_str)
print('Decrypted JSON Payload with CBC:', decrypted_json_payload)

# Encrypt the JSON string
encrypted_json_str = encryptGCM(json_str, password)
print('Encrypted JSON with GCM:', encrypted_json_str)

# Decrypt the JSON string
decrypted_json_str = decryptGCM(encrypted_json_str, password)
print('Decrypted JSON with GCM:', decrypted_json_str)

# Convert decrypted JSON string back to dictionary
decrypted_json_payload = json.loads(decrypted_json_str)
print('Decrypted JSON Payload with GCM:', decrypted_json_payload)