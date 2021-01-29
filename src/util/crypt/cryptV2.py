from cryptography.fernet import Fernet

def decryptV2(key: bytes, data: bytes) -> bytes:

    return Fernet(key).decrypt(data)

def encryptV2(key: bytes, data: bytes) -> bytes:

    return Fernet(key).encrypt(data)

def generate_keyV2() -> bytes:

    return Fernet.generate_key()
