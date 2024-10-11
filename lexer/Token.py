class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self._token_type = token_type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def __repr__(self):
        return f'|{self._token_type} {self._lexeme} {self._literal}|'

    def get_token_type(self):
        return self._token_type

    def get_line(self):
        return self._line

    def get_literal(self):
        return self._literal

    def get_lexeme(self):
        return self._lexeme
