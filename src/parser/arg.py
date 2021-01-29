from argparse import ArgumentParser

class ArgParser(ArgumentParser):

    def __init__(self, description = None):

        ArgumentParser.__init__(self, description = description)

        self.add_argument(
            "password", help = "Your password."
            )

        self.add_argument(
            "--set", metavar = "new_password", dest = "new_password",
            help = "Change the password."
            )

        self.add_argument(
            "--list", action = "store_true", dest = "list",
            help = "Show a list of all the namespaces."
            )

        namespace = self.add_argument_group("namespace arguments")

        namespace.add_argument(
            "namespace", nargs = "?", help = "Namespace assigned to a directory.", default = ""
            )

        namespace.add_argument(
            "-r", metavar = "dir", dest = "register",
            help = "Register the password for a directory."
            )

        namespace.add_argument(
            "-l", action = "store_true", dest = "lock",
            help = "Lock a folder."
            )

        namespace.add_argument(
            "-u", action = "store_true", dest = "unlock",
            help = "Unlock a folder."
            )

        namespace.add_argument(
            "-d", action = "store_true", dest = "delete",
            help = "Delete a folder and its namespace from the database."
            )

        namespace.add_argument(
            "-s", action = "store_true", dest = "show",
            help = "Show in explorer."
            )
