from src.client import execute, show_error, show_message, show_warning
from src.manager import Manager
from src.parser.arg import ArgParser
import colorama

# Initialize Colorama.
colorama.init()

# Get the arguments.
arg_parser = ArgParser(description = None)
args = arg_parser.parse_args()

try:
    # Initialize the manager.
    manager = Manager(args.password, show_message, show_warning)

    # Execute the command.
    execute(manager, args)

except Exception as error:
    show_error(error)
