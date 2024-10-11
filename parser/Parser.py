from lexer import TokenType, SyntaxException
from parser.nodes import (
    AssignmentNode,
    BlockNode,
    NumberLiteralNode,
    PrintNode,
    StringLiteralNode,
    VariableNode
)


class Parser:
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = 0

    def parse(self):
        nodes = []
        while self._current < len(self._tokens) and not self._is_eof_token():
            node = self._handle_token()
            nodes.append(node)
        return BlockNode(nodes)

    def _handle_token(self):
        token = self._tokens[self._current]
        if token.get_token_type() == TokenType.PRINT:
            return self._parse_print_token()
        if token.get_token_type() == TokenType.STRING:
            return self._parse_string_token()
        if token.get_token_type() == TokenType.NUMBER:
            return self._parse_number_token()
        if token.get_token_type() == TokenType.IDENTIFIER:
            return self._parse_identifier_token()
        if token.get_token_type() == TokenType.VAR:
            return self._parse_var_token()

    def _parse_print_token(self):
        self._validate_token({TokenType.LEFT_PAREN}, "Expected '(' for print statement.")
        self._validate_token(TokenType.valid_print_types(), "Incompatible value for print.")
        node_to_print = self._handle_token()
        self._validate_token({TokenType.RIGHT_PAREN}, "Expected ')' to close print statement.")
        self._validate_token({TokenType.SEMI_COLON}, "Expected ';' to terminate statement.")
        self._current += 1
        return PrintNode(node_to_print)

    def _parse_string_token(self):
        string_token = self._tokens[self._current]
        return StringLiteralNode(string_token.get_literal())

    def _parse_number_token(self):
        number_token = self._tokens[self._current]
        return NumberLiteralNode(number_token.get_literal())

    def _parse_identifier_token(self):
        identifier_token = self._tokens[self._current]
        return VariableNode(identifier_token.get_lexeme())

    def _parse_var_token(self):
        self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for assignment.")
        variable_node = self._handle_token()
        self._validate_token({TokenType.EQUAL}, "Expected '✍️' for assignment.")
        self._validate_token(TokenType.valid_assignment_types(), "Incompatible value for assignment.")
        value_node = self._handle_token()
        self._validate_token({TokenType.SEMI_COLON}, "Expected ';' to terminate the statement.")
        self._current += 1
        return AssignmentNode(variable_node, value_node)

    def _validate_token(self, expected_token_types, error_message):
        next_index = self._current + 1
        if self._in_bounds(next_index):
            next_token = self._tokens[next_index]
            if next_token.get_token_type() not in expected_token_types:
                raise SyntaxException(next_token.get_line(), error_message)
            self._current = next_index

    def _in_bounds(self, index):
        return index < len(self._tokens)

    def _is_eof_token(self):
        token = self._tokens[self._current]
        return token.get_token_type() == TokenType.EOF
