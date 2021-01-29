from colorama import Fore, Style

def show_message(message, end = "\n"):

    print(Style.RESET_ALL + str(message), end = end)

def show_warning(message, end = "\n"):

    print(Fore.YELLOW + str(message), end = end)

def show_error(message, end = "\n"):

    print(Fore.RED + str(message), end = end)
