from .token import Token
from .token_type import TokenType
from .syntax_exception import SyntaxException


class Lexer:
    """
    The Lexer class is responsible for scanning the source code and converting it into a list of tokens.

    It processes the source code character by character, grouping characters into tokens based on the
    predefined rules of the mojilang language. It also tracks line numbers for error reporting.
    """

    def __init__(self, source):
        """
        Initializes the Lexer with the source code to be scanned.

        :param source: The source code as a string.
        """
        self._source = source

        self._exceptions = []
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 1

    def scan_tokens(self):
        """
        Scans the source code and generates a list of tokens.

        This method loops through the source code, scanning each character until
        the end of the source is reached. Once all tokens are scanned, an EOF token is added.
        """
        while not self._is_at_end():
            self._start = self._current
            self._scan_token()

        end_of_file_token = Token(TokenType.EOF, "", None, self._line)
        self._tokens.append(end_of_file_token)

    def _is_at_end(self):
        """
        Checks if the lexer has reached the end of the source code.

        :return: True if the current index is at or beyond the end of the source, False otherwise.
        """
        return self._current >= len(self._source)

    def _scan_token(self):
        """
        Scans the next character in the source code and converts it into a token.

        Depending on the character, this method generates the appropriate token or handles
        special cases like whitespace, comments, strings, and numbers.
        """
        character = self._advance()
        if character == '(':
            self._add_token(TokenType.LEFT_PAREN)
        elif character == ')':
            self._add_token(TokenType.RIGHT_PAREN)
        elif character == '{':
            self._add_token(TokenType.LEFT_BRACE)
        elif character == '}':
            self._add_token(TokenType.RIGHT_BRACE)
        elif character == ';':
            self._add_token(TokenType.SEMI_COLON)
        elif character == '✍':
            self._add_token(TokenType.EQUAL)
        elif character == '🤝':
            self._add_token(TokenType.EQUAL_EQUAL)
        elif character == '🙅':
            self._add_token(TokenType.BANG_EQUAL if self._match('🤝') else TokenType.BANG)
        elif character == '👇':
            self._add_token(TokenType.LESS_EQUAL if self._match('🤝') else TokenType.LESS)
        elif character == '☝':
            self._add_token(TokenType.GREATER_EQUAL if self._match('🤝') else TokenType.GREATER)
        elif character == '🖊':
            self._add_token(TokenType.INPUT)
        elif character == '💥':
            self._add_token(TokenType.BREAK)
        elif character == '🤓':
            self._add_token(TokenType.CONTINUE)
        elif character == '🫡':
            self._add_token(TokenType.RETURN)
        elif character == '🛠':
            self._add_token(TokenType.FUNCTION)
        elif character == '😤':
            self._add_token(TokenType.TRUE)
        elif character == '😔':
            self._add_token(TokenType.FALSE)
        elif character == '🤔':
            self._add_token(TokenType.IF)
        elif character == '🙈':
            self._add_token(TokenType.ELSEIF)
        elif character == '💅':
            self._add_token(TokenType.ELSE)
        elif character == '🔁':
            self._add_token(TokenType.LOOP)
        elif character == '🗣':
            self._add_token(TokenType.PRINT)
        elif character == '🥸':
            self._add_token(TokenType.VAR)
        elif character == '➕':
            self._add_token(TokenType.PLUS)
        elif character == '➖':
            self._add_token(TokenType.MINUS)
        elif character == '✖':
            self._add_token(TokenType.MULTIPLY)
        elif character == '➗':
            self._add_token(TokenType.DIVIDE)
        elif character == '🍕':
            self._add_token(TokenType.MODULUS)
        elif character == '🥕':
            self._add_token(TokenType.EXPONENT)
        elif character == '🧐':
            while self._peek() != '\n' and not self._is_at_end():
                self._advance()
        elif character in [' ', '\r', '\t', '\n']:
            if character == '\n':
                self._line += 1
        elif character == '"':
            self._string()
        else:
            if character.isdigit():
                self._number()
            elif character.isalnum():
                if self._peek_next(2) == 'and':
                    self._current += 2
                    self._add_token(TokenType.AND)
                elif self._peek_next(1) == 'or':
                    self._current += 1
                    self._add_token(TokenType.OR)
                else:
                    self._identifier()
            else:
                unexpected_character_exception = SyntaxException(self._line, "Unexpected character.")
                self._exceptions.append(unexpected_character_exception)

    def _advance(self):
        """
        Advances the current index and returns the next character from the source code.

        :return: The current character at the current index.
        """
        character = self._source[self._current]
        self._current += 1
        return character

    def _add_token(self, token_type, literal=None):
        """
        Adds a new token to the list of scanned tokens.

        :param token_type: The type of the token (e.g., LEFT_PAREN, NUMBER).
        :param literal: The literal value of the token, if applicable (e.g., for strings or numbers).
        """
        text = self._source[self._start:self._current]
        new_token = Token(token_type, text, literal, self._line)
        self._tokens.append(new_token)

    def _match(self, expected):
        """
        Checks if the next character matches the expected character, and advances if it does.

        :param expected: The character to match.
        :return: True if the expected character matches, False otherwise.
        """
        if self._is_at_end():
            return False
        if self._source[self._current] != expected:
            return False
        self._current += 1
        return True

    def _peek(self):
        """
        Returns the next character in the source without advancing the index.

        :return: The next character or '\0' if at the end of the source.
        """
        if self._is_at_end():
            return '\0'
        return self._source[self._current]

    def _string(self):
        """
        Handles string literals by scanning until the closing quotation mark or end of the source.

        Raises a SyntaxException if the string is unterminated.
        """
        while self._peek() != '"' and not self._is_at_end():
            if self._peek() == '\n':
                self._line += 1
            self._advance()

        if self._is_at_end():
            unterminated_string_exception = SyntaxException(self._line, "Unterminated string.")
            self._exceptions.append(unterminated_string_exception)

        self._advance()

        value = self._source[self._start + 1: self._current - 1]
        self._add_token(TokenType.STRING, value)

    def _number(self):
        """
        Scans a numeric literal, handling integers and floating-point numbers.
        """
        while self._peek().isdigit():
            self._advance()

        if self._peek() == '.':
            self._advance()
            while self._peek().isdigit():
                self._advance()

        number = self._source[self._start: self._current]
        self._add_token(TokenType.NUMBER, float(number))

    def _peek_next(self, next_count):
        """
        Peeks ahead to check the next 'next_count' characters without advancing the index.

        :param next_count: The number of characters to peek ahead.
        :return: The substring starting from the current position up to next_count characters.
        """
        next_index = self._current + next_count
        if next_index >= len(self._source):
            return '\0'
        return self._source[self._start:next_index]

    def _identifier(self):
        """
        Scans an identifier (variable name or keyword) from the source code.
        """
        while self._peek().isalnum():
            self._advance()
        self._add_token(TokenType.IDENTIFIER)

    def get_tokens(self):
        """
        Returns the list of tokens that have been scanned.

        :return: A list of Token objects.
        """
        return self._tokens
