class Token:
    """
    The Token class represents a single token in the EmoLang source code.

    A token consists of a type, a lexeme (the string representation of the token),
    an optional literal value (such as a number or string), and the line number
    where the token appears in the source code.
    """

    def __init__(self, token_type, lexeme, literal, line):
        """
        Initializes a Token instance with its type, lexeme, literal value, and line number.

        :param token_type: The type of the token (e.g., IDENTIFIER, NUMBER, PLUS).
        :param lexeme: The exact string representation of the token in the source code.
        :param literal: The literal value of the token (if applicable), such as a number or string.
        :param line: The line number where the token appears in the source code.
        """
        self._token_type = token_type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def __repr__(self):
        """
        Returns a string representation of the token, useful for debugging.

        :return: A formatted string containing the token type, lexeme, and literal value.
        """
        return f'|{self._token_type} {self._lexeme} {self._literal}|'

    def get_token_type(self):
        return self._token_type

    def get_line(self):
        return self._line

    def get_literal(self):
        return self._literal

    def get_lexeme(self):
        return self._lexeme

    def is_token_type(self, token_type):
        """
        Checks if the token is of the specified type.

        :param token_type: The type to compare against the token's type.
        :return: True if the token matches the specified type, False otherwise.
        """
        return self._token_type == token_type
