class SyntaxException(Exception):
    """
    Custom exception class for handling syntax errors in the mojilang interpreter.

    Raised when a syntax error is encountered during parsing or execution of the program.
    Stores the line number where the error occurred and a descriptive error message.
    """

    def __init__(self, line, message):
        """
        Initializes the SyntaxException with a specific line number and error message.

        :param line: The line number where the syntax error occurred.
        :param message: A descriptive message explaining the nature of the syntax error.
        """
        super().__init__(f"Syntax error at line {line}: {message}")
        self._line = line
        self._message = message
