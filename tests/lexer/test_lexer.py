from emolang.lexer import Lexer, TokenType


class TestLexer:
    def _get_tokens(self, source_code):
        lexer = Lexer(source_code)
        lexer.scan_tokens()
        return lexer.get_tokens()

    def _assert_tokens(self, tokens, expected_tokens):
        for i in range(len(tokens)):
            assert tokens[i].is_token_type(expected_tokens[i])

    def test_variable_declaration(self):
        source_code = "🥸 variable ✍️ 3;"
        tokens = self._get_tokens(source_code)
        expected_tokens = [
            TokenType.VAR,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.NUMBER,
            TokenType.SEMI_COLON,
            TokenType.EOF
        ]
        assert len(tokens) == len(expected_tokens)
        self._assert_tokens(tokens, expected_tokens)
        assert tokens[1].get_lexeme() == "variable"
        assert tokens[3].get_literal() == 3

    def test_boolean_tokens(self):
        source_code = "🥸 variable ✍️ 😤 and 😔;"
        tokens = self._get_tokens(source_code)
        expected_tokens = [
            TokenType.VAR,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.TRUE,
            TokenType.AND,
            TokenType.FALSE,
            TokenType.SEMI_COLON,
            TokenType.EOF
        ]
        assert len(tokens) == len(expected_tokens)
        self._assert_tokens(tokens, expected_tokens)
