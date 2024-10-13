from lexer import TokenType, SyntaxException
from parser.nodes import (
    AssignmentNode,
    AdditionNode,
    MultiplicationNode,
    SubtractionNode,
    ModulusNode,
    DivisionNode,
    ExponentNode,
    BlockNode,
    NumberLiteralNode,
    PrintNode,
    StringLiteralNode,
    VariableNode,
    OperationContext
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

    def _handle_token(self, index=None, context=None):
        if index is None:
            index = self._current
        token = self._retrieve_token(index)
        if token.get_token_type() == TokenType.PRINT:
            return self._parse_print_token()
        if token.get_token_type() == TokenType.STRING:
            return self._parse_string_token()
        if token.get_token_type() == TokenType.NUMBER:
            return self._parse_number_token(index)
        if token.get_token_type() == TokenType.IDENTIFIER:
            return self._parse_identifier_token()
        if token.get_token_type() == TokenType.VAR:
            return self._parse_var_token()
        if token.get_token_type() == TokenType.EQUAL:
            expression = self._parse_expression()
            return expression
        if token.get_token_type() in TokenType.operation_types():
            return self._parse_operation(token, context)

    def _parse_operation(self, token, context):
        if token.get_token_type() == TokenType.PLUS:
            return AdditionNode(context.get_left_operand(), context.get_right_operand())
        if token.get_token_type() == TokenType.MINUS:
            return SubtractionNode(context.get_left_operand(), context.get_right_operand())
        if token.get_token_type() == TokenType.MULTIPLY:
            return MultiplicationNode(context.get_left_operand(), context.get_right_operand())
        if token.get_token_type() == TokenType.DIVIDE:
            return DivisionNode(context.get_left_operand(), context.get_right_operand())
        if token.get_token_type() == TokenType.MODULUS:
            return ModulusNode(context.get_left_operand(), context.get_right_operand())
        if token.get_token_type() == TokenType.EXPONENT:
            return ExponentNode(context.get_left_operand(), context.get_right_operand())

    def _parse_print_token(self):
        self._validate_token({TokenType.LEFT_PAREN}, "Expected '(' for print statement.")
        self._validate_token(TokenType.valid_print_types(), "Incompatible value for print.")
        node_to_print = self._handle_token()
        self._validate_token({TokenType.RIGHT_PAREN}, "Expected ')' to close print statement.")
        self._validate_token({TokenType.SEMI_COLON}, "Expected ';' to terminate statement.")
        self._current += 1
        return PrintNode(node_to_print)

    def _parse_string_token(self):
        string_token = self._current_token()
        return StringLiteralNode(string_token.get_literal())

    def _parse_number_token(self, index):
        number_token = self._retrieve_token(index)
        return NumberLiteralNode(number_token.get_literal())

    def _parse_identifier_token(self):
        identifier_token = self._current_token()
        return VariableNode(identifier_token.get_lexeme())

    def _parse_var_token(self):
        self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for assignment.")
        variable_node = self._handle_token()
        self._validate_token({TokenType.EQUAL}, "Expected '✍️' for assignment.")
        value_node = self._handle_token()
        self._current = self._find_next_semicolon_index() - 1
        self._validate_token({TokenType.SEMI_COLON}, "Expected ';' to terminate the statement.")
        self._current += 1
        return AssignmentNode(variable_node, value_node)

    def _parse_expression(self):
        end_of_expression_index = self._find_next_semicolon_index()
        node = self._parse_expression_recursive(self._current + 1, end_of_expression_index - 1)
        if not node:
            raise SyntaxException(self._current_token().get_line(), "Invalid expression: no valid operations found.")
        return node

    def _find_next_semicolon_index(self):
        index = self._current
        while self._retrieve_token(index).get_token_type() != TokenType.SEMI_COLON and self._retrieve_token(index).get_token_type() != TokenType.EOF:
            index += 1
        return index

    def _parse_expression_recursive(self, left_index, right_index):
        left_token, right_token = self._retrieve_token(left_index), self._retrieve_token(right_index)
        index_delta = right_index - left_index
        if index_delta < 0:
            raise SyntaxException(left_token.get_line(), 'right_index less than left_index')
        if index_delta == 0:
            return self._handle_token(left_index)
        if self._within_parens(left_token, right_token):
            return self._parse_expression_recursive(left_index + 1, right_index - 1)
        operator_precedence = [
            {TokenType.MINUS, TokenType.PLUS},
            {TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULUS},
            {TokenType.EXPONENT}
        ]
        for operators in operator_precedence:
            index = left_index
            while index < right_index:
                index = self._skip_parentheses(index, right_index)
                node = self._divide_by_operations(operators, left_index, right_index, index)
                if node:
                    return node
                index += 1

    def _skip_parentheses(self, left_index, right_index):
        paren_counter = 0
        while left_index <= right_index:
            token = self._retrieve_token(left_index)
            if token.get_token_type() == TokenType.LEFT_PAREN:
                paren_counter += 1
            if token.get_token_type() == TokenType.RIGHT_PAREN:
                paren_counter -= 1
            if paren_counter == 0:
                break
            left_index += 1
        return left_index + 1

    def _divide_by_operations(self, operations, left_index, right_index, index):
        token = self._retrieve_token(index)
        if token.get_token_type() in operations:
            left_node = self._parse_expression_recursive(left_index, index - 1)
            right_node = self._parse_expression_recursive(index + 1, right_index)
            if left_node is None or right_node is None:
                raise SyntaxException(token.get_line(), "Invalid expression: missing left or right operand.")

            context = OperationContext(left_node, right_node)
            return self._handle_token(index, context)

    def _within_parens(self, left_token, right_token):
        return left_token.get_token_type() == TokenType.LEFT_PAREN and right_token.get_token_type() == TokenType.RIGHT_PAREN

    def _validate_token(self, expected_token_types, error_message):
        next_index = self._current + 1
        if self._in_bounds(next_index):
            next_token = self._retrieve_token(next_index)
            if next_token.get_token_type() not in expected_token_types:
                raise SyntaxException(next_token.get_line(), error_message)
            self._current = next_index

    def _in_bounds(self, index):
        return index < len(self._tokens)

    def _is_eof_token(self):
        token = self._current_token()
        return token.get_token_type() == TokenType.EOF

    def _current_token(self):
        return self._retrieve_token(self._current)

    def _retrieve_token(self, index):
        return self._tokens[index]
