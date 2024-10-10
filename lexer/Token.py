class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self._token_type = token_type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def __repr__(self):
        return f'|{self._token_type} {self._lexeme} {self._literal}|'
