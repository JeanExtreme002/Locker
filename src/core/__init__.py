from ..util import crypt
from subprocess import getoutput
import os

uuid = getoutput("wmic csproduct get uuid").split("\n\n")[1].strip()
key = sum([ord(char) for char in uuid])

paths = {
    "database": os.path.join(os.environ["APPDATA"], crypt.encryptV1(key, "lockerDB", to_hex = True))
    }
