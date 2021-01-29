from .display import show_message

def change_password(manager, new_password):

    manager.change_password(new_password)
    show_message("Password changed successfully.\n")

def delete(manager, namespace):

    namespace = namespace.upper()

    manager.delete(namespace)
    show_message("%s successfully deleted.\n" % namespace)

def lock(manager, namespace):

    namespace = namespace.upper()

    manager.lock(namespace)
    show_message("%s successfully locked.\n" % namespace)

def unlock(manager, namespace):

    namespace = namespace.upper()

    manager.unlock(namespace)
    show_message("%s successfully unlocked.\n" % namespace)

def register(manager, namespace, path):

    namespace = namespace.upper()

    manager.register(namespace, path)
    show_message("%s successfully registered.\n" % namespace)

def show_in_explorer(manager, namespace):

    namespace = namespace.upper()
    manager.show_dir_in_explorer(namespace)

def show_namespaces(manager):

    namespaces = manager.show_namespaces()

    show_message("\nNAMESPACES:" + (" EMPTY" if not namespaces else ""))
    for n in namespaces: show_message("- " + n)
