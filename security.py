from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data: bytes) -> bytes:
    return cipher.encrypt(data)

def decrypt_data(encrypted_data: bytes) -> bytes:
    return cipher.decrypt(encrypted_data)