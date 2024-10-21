from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(chunk_path, key):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(chunk_path, 'rb') as infile:
        data = infile.read()
        encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(f"{chunk_path}.enc", 'wb') as outfile:
        outfile.write(iv + encrypted_data)

def decrypt_file(encrypted_file_path, key):
    backend = default_backend()
    with open(encrypted_file_path, 'rb') as infile:
        iv = infile.read(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
        decryptor = cipher.decryptor()

        encrypted_data = infile.read()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(f"{encrypted_file_path}_decrypted", 'wb') as outfile:
        outfile.write(decrypted_data)
