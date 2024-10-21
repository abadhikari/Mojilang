import sys
import argparse

from mojilang.lexer import Lexer
from mojilang.parser import Parser
from mojilang.interpreter import Interpreter
from mojilang.lexer import SyntaxException


def main(source_code):
    """
    Main function that initializes the Lexer, Parser, and Interpreter
    to run Mojilang code from the provided source code.

    :param source_code: The source code of Mojilang program as a string.
    """
    # Initialize Lexer and scan token
    lexer = Lexer(source_code)
    exceptions = lexer.scan_tokens()
    if exceptions:
        raise SyntaxException(12, f'Found the following syntax errors: {exceptions}')
    tokens = lexer.get_tokens()

    # Initialize Parser
    parser = Parser(tokens)
    abstract_syntax_tree = parser.parse()

    # Initialize Interpreter and run it
    interpreter = Interpreter(abstract_syntax_tree)
    interpreter.execute()


def run_cli():
    """Set up the CLI allowing the user to provide the Mojilang file path to execute."""
    parser = argparse.ArgumentParser(description="Run a Mojilang program from a .moji file.")

    parser.add_argument(
        'filepath',
        type=str,
        help='The path to the .moji file containing the Mojilang source code.'
    )

    args = parser.parse_args()
    if not args.filepath.endswith('.moji'):
        print(f"Error: The file '{args.filepath}' must have a '.moji' extension.")
        sys.exit(1)

    return args.filepath


def read_source_code(file_path):
    """
    Reads the source code from the provided file path.

    :param file_path: The path to the Mojilang source code file.
    :return: The content of the file as a string.
    :raises FileNotFoundError: If the file does not exist.
    :raises Exception: If any other error occurs during file reading.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    """Entry point for Mojilang."""
    f_path = run_cli()
    source = read_source_code(f_path)
    main(source)
