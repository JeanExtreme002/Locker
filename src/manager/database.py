from ..util import crypt
from ..util import system
import json
import os

class Database(object):

    def __init__(self, filename):

        self.__filename = filename
        self.__data = dict()

        # Get the data from the database.
        self.__create() if not os.path.exists(filename) else self.__load_data()

    def __create(self):

        # Generate a key and create the database.
        self.__key = crypt.generate_keyV2()
        self.__update_database()

    def __decrypt(self, key, data):

        # Return the decrypted data.
        return json.loads(crypt.decryptV2(key, data).decode())

    def __encrypt(self, key, data):

        # Return the encrypted data.
        return crypt.encryptV2(key, json.dumps(data).encode())

    def __load_data(self):

        # Open the file and get its data.
        with open(self.__filename, "rb") as file:
            key, data = file.read().split("=".encode(), maxsplit = 1)

        # Get the key and decrypt the data.
        self.__key = key + "=".encode()
        self.__data = self.__decrypt(self.__key, data)

    def __update_database(self):

        # Encrypt the data.
        data = self.__encrypt(self.__key, self.__data)

        # Show the file.
        system.set_dir_attr("-H", self.__filename, all = False)

        # Save the data to the file.
        with open(self.__filename, "wb") as file:
            file.write(self.__key + data)

        # Show the file.
        system.set_dir_attr("+H", self.__filename, all = False)

    def get_data(self):

        # Return a copy of the data.
        return self.__data.copy()

    def get_key(self):

        # Return the sum of the key characters.
        return sum([ord(char) for char in self.__key.decode()])

    def update(self, data):

        # Update the data in the database.
        self.__data = data.copy()
        self.__update_database()
