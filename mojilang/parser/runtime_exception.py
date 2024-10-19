class RuntimeException(Exception):
    """ A custom exception class for handling mojilang-specific runtime errors."""
    def __init__(self, message, line_number=None):
        full_message = ""
        if line_number is not None:
            full_message += f"line {line_number}, "
        full_message += f"mojilang Runtime Error: {message}"
        super().__init__(full_message)
