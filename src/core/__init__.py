from ..util import crypt
import os

key = sum([ord(char) for char in os.getlogin()]) // 100 + 1

paths = {
    "database": os.path.join(os.environ["APPDATA"], crypt.encryptV1(key, "lockerDB", to_hex = True))
    }
