from .display import *
from .functions import *

def execute(manager, args):

    """
    Run the functions according to the given arguments.
    """

    if args.new_password and args.new_password != args.password:
        change_password(manager, args.new_password)

    if args.register:
        register(manager, args.namespace, args.register)

    if args.lock:
        lock(manager, args.namespace)

    if args.unlock and not args.delete and not args.register:
        unlock(manager, args.namespace)

    if args.delete:
        unlock(manager, args.namespace)
        delete(manager, args.namespace)

    if args.show:
        show_in_explorer(manager, args.namespace)

    if args.list:
        show_namespaces(manager)
