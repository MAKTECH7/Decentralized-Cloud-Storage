from encryption import encrypt_file, decrypt_file

# Define your encryption key (must be 16 bytes for AES)
key = b'Sixteen byte key'

# Test file names
original_file = 'test_chunk.txt'  # Ensure this file exists before running
encrypted_file = 'test_chunk.txt.enc'

# Encrypt the file
encrypt_file(original_file, key)
print(f"{original_file} has been encrypted to {encrypted_file}")

# Decrypt the file
decrypt_file(encrypted_file, key)
print(f"{encrypted_file} has been decrypted back to {original_file}")