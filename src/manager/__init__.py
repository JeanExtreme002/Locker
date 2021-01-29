from ..core import paths
from ..util import crypt, system
from .database import Database
from .errors import *
import hashlib
import os

class Manager(object):

    def __init__(self, password, msg_callback, err_callback):

        # Instantiate the parameters.
        self.__message_callback = msg_callback
        self.__error_callback = err_callback
        self.__database_fn = paths["database"]

        # Initialize the database.
        self.__database = Database(self.__database_fn)

        # Get the password key.
        self.__password_key = crypt.encryptV1(self.__database.get_key(), "#password", to_hex = True)

        # Validate the password.
        self.__validate_password(password)

    def __get_hash(self, string):

        # Return a hash of a string.
        return hashlib.sha512(string.encode()).hexdigest()

    def __validate_password(self, password):

        # Get the data from the database.
        data = self.__database.get_data()

        # Get the valid password.
        valid_password = data.get(self.__password_key)

        # Check if there is a password saved in the database.
        if not valid_password:

            # Register the password in the database for the first time.
            valid_password = self.change_password(password)

        # Inform that it is validating the password.
        self.__message_callback("Validating password...")

        # Check if the password is valid.
        if not valid_password == self.__get_hash(password):
            raise InvalidPasswordError

    def change_password(self, new_password):

        # Get the data from the database.
        data = self.__database.get_data()

        # Get the hash of the password.
        new_password = self.__get_hash(new_password)

        # Change the password.
        self.__message_callback("Registering the password in the database...")

        data[self.__password_key] = new_password
        self.__database.update(data)

        return new_password

    def register(self, namespace, path):

        # Get the data from the database.
        data = self.__database.get_data()

        # Check if a namespace has been passed.
        if not namespace:
            raise NoNamespaceError

        # Check if the namespace exists in the database.
        if namespace in data:
            raise NamespaceExistsError

        # Check if the path is registered in the database.
        if path in data.values():
            raise PathRegisteredError

        # Check if it is a folder and if it exists.
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FolderNotFoundError

        # Register the directory in database.
        self.__message_callback("Registering the directory in the database...")

        data[namespace] = path
        self.__database.update(data)

    def show_namespaces(self):

        # Get the data from the database.
        data = self.__database.get_data()

        # Remove the password.
        data.pop(self.__password_key)

        # Return a list of namespaces.
        return data.keys()

    def lock(self, namespace):

        # Get the data from the database.
        data = self.__database.get_data()

        # Check if a namespace has been passed.
        if not namespace:
            raise NoNamespaceError

        # Check if the namespace exists.
        if not namespace in data:
            raise NamespaceNotExistsError

        # Get the path.
        path = data[namespace]

        # Check if it is a folder and if it exists.
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FolderNotFoundError

        # Lock the folder.
        self.__message_callback("Locking the directory... Do not end the process.")
        self.__message_callback("Encrypting...")

        system.encrypt_dir(self.__database.get_key(), path, self.__message_callback, self.__error_callback)
        system.set_dir_attr("+R +A +S +H +I", path, all = True)

    def unlock(self, namespace):

        # Get the data from the database.
        data = self.__database.get_data()

        # Check if a namespace has been passed.
        if not namespace:
            raise NoNamespaceError

        # Check if the namespace exists.
        if not namespace in data:
            raise NamespaceNotExistsError

        # Get the path.
        path = data[namespace]

        # Check if it is a folder and if it exists.
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FolderNotFoundError

        # Unlock the folder.
        self.__message_callback("Unlocking the directory... Do not end the process.")
        system.set_dir_attr("-R -A -S -H -I", path, all = True)

        self.__message_callback("Decrypting...")
        system.decrypt_dir(self.__database.get_key(), path, self.__message_callback, self.__error_callback)

    def delete(self, namespace):

        # Get the data from the database.
        data = self.__database.get_data()

        # Check if the namespace exists.
        if namespace in data:

            # Delete the directory and its namespace.
            self.__message_callback("Removing the directory from the database...")

            data.pop(namespace)
            self.__database.update(data)

    def show_dir_in_explorer(self, namespace):

        # Get the data from the database.
        data = self.__database.get_data()

        # Check if a namespace has been passed.
        if not namespace:
            raise NoNamespaceError

        # Check if the namespace exists.
        if not namespace in data:
            raise NamespaceNotExistsError

        # Get the path.
        path = data[namespace]

        # Show the folder in explorer.
        self.__message_callback("Opening the directory in explorer...")
        system.show_in_explorer(path)
