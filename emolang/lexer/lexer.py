from .token import Token
from .token_type import TokenType
from .syntax_exception import SyntaxException


class Lexer:
    def __init__(self, source):
        self._source = source

        self._exceptions = []
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 1

    def scan_tokens(self):
        while not self._is_at_end():
            self._start = self._current
            self._scan_token()

        end_of_file_token = Token(TokenType.EOF, "", None, self._line)
        self._tokens.append(end_of_file_token)

    def _is_at_end(self):
        return self._current >= len(self._source)

    def _scan_token(self):
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
        character = self._source[self._current]
        self._current += 1
        return character

    def _add_token(self, token_type, literal=None):
        text = self._source[self._start:self._current]
        new_token = Token(token_type, text, literal, self._line)
        self._tokens.append(new_token)

    def _match(self, expected):
        if self._is_at_end():
            return False
        if self._source[self._current] != expected:
            return False
        self._current += 1
        return True

    def _peek(self):
        if self._is_at_end():
            return '\0'
        return self._source[self._current]

    def _string(self):
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
        while self._peek().isdigit():
            self._advance()

        if self._peek() == '.':
            self._advance()
            while self._peek().isdigit():
                self._advance()

        number = self._source[self._start: self._current]
        self._add_token(TokenType.NUMBER, float(number))

    def _peek_next(self, next_count):
        next_index = self._current + next_count
        if next_index >= len(self._source):
            return '\0'
        return self._source[self._start:next_index]

    def _identifier(self):
        while self._peek().isalnum():
            self._advance()
        self._add_token(TokenType.IDENTIFIER)

    def get_tokens(self):
        return self._tokens
