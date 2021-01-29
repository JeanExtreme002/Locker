from .crypt import decryptV1, encryptV1
from subprocess import getoutput
import os

def encrypt_dir(key, path, msg_callback = None, err_callback = None):

    # Get all folders and files from the directory.
    paths = [(dir_, basename) for dir_, basename in get_all(path) if not basename.startswith("$_$")]
    progress, total = 0, len(paths)

    for dir_, basename in paths:

        # Encrypt the basename.
        old, new = os.path.join(dir_, basename), "$_$" + encryptV1(key, basename)

        # Rename the directory.
        if rename(old, new) and err_callback:
            err_callback("\rERROR: Could not encrypt the directory name \"%s\" to \"%s\"." % (basename, new))

        # Calculate and send the progress.
        if msg_callback:
            progress += 1
            msg_callback("\rProgress: %.1f%%" % (100 / total * progress), end = "")

    if msg_callback: msg_callback("\rProgress: 100.0%")

def decrypt_dir(key, path, msg_callback = None, err_callback = None):

    # Get all folders and files from the directory.
    paths = [(dir_, basename) for dir_, basename in get_all(path) if basename.startswith("$_$")]
    progress, total = 0, len(paths)

    for dir_, basename in paths:

        # Decrypt the basename.
        old, new = os.path.join(dir_, basename), decryptV1(key, basename.lstrip("$_$"))

        # Rename the directory.
        if rename(old, new) and err_callback:
            err_callback("\rERROR: Could not decrypt the directory name \"%s\" to \"%s\"." % (basename, new))

        # Calculate and send the progress.
        if msg_callback:
            progress += 1
            msg_callback("\rProgress: %.1f%%" % (100 / total * progress), end = "")

    if msg_callback: msg_callback("\rProgress: 100.0%")

def get_all(path):

    # Return each folder and file in a directory.
    for dir_, folders, files in os.walk(path, topdown = False):
        for basename in files + folders: yield (dir_, basename)

def rename(old, new):

    # Rename a file or directory.
    return getoutput("REN \"%s\" \"%s\"" % (old, new))

def set_dir_attr(attributes, path, all = True):

    # Get the path and the command.
    path = path.rstrip(os.path.sep)
    command = "ATTRIB " + attributes + " \"%s\""

    # Set the attributes.
    getoutput(command % path)
    if all: getoutput((command + " /S /D") % os.path.join(path, "*"))

def show_in_explorer(path):

    # Show directory in explorer.
    return getoutput("explorer %s" % path)
