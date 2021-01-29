class FolderNotFoundError(Exception):
    def __str__(self):
        return "This folder does not exist."

class InvalidPasswordError(Exception):
    def __str__(self):
        return "This password is incorrect."

class NamespaceExistsError(Exception):
    def __str__(self):
        return "This namespace is already in use."

class NamespaceNotExistsError(Exception):
    def __str__(self):
        return "This namespace does not exist."

class NoNamespaceError(Exception):
    def __str__(self):
        return "Please enter a namespace."

class PathRegisteredError(Exception):
    def __str__(self):
        return "This path is already registered."
