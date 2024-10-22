from mojilang.lexer import TokenType, SyntaxException
from mojilang.parser.nodes import (
    BinaryOperationContext,
    UnaryOperationContext,
)


class ExpressionParser:
    """
    The ExpressionParser class is responsible for parsing expressions in the mojilang source code.
    It handles the logic required to process expressions, such as arithmetic and logical
    operations, ensuring that they are evaluated following operator precedence and parentheses
    and finally converts them into AST nodes.

    Attributes:
        _parser (Parser): A reference to the main parser instance, which allows this class to delegate
                          other parts of the parsing process.
        _state (ParserState): A reference to the current state of the parser, which manages tokens,
                              token positions, and block scopes.
    """
    def __init__(self, parser):
        """
        Initializes the ExpressionParser with a reference to the main parser and its state.

        :param parser: The main Parser instance, which this class uses to delegate
                       other parsing tasks.
        """
        self._parser = parser
        self._state = parser.get_state()

    def parse(self, end_tokens=None):
        """
        Parses an expression up to the specified end token (such as a semicolon or a right brace).

        :param: end_tokens: optional tokens that the expression end on. Used to exit early.
        :return: The root node of the parsed expression.
        """
        if end_tokens is None:
            end_tokens = {}
        end_of_expression_index = self._find_end_of_expression_index(end_tokens)
        node = self._parse_expression_recursive(self._state.get_current(), end_of_expression_index - 1)
        self._state.set_current(end_of_expression_index)
        return node

    def _find_end_of_expression_index(self, end_tokens):
        """
        Finds the index of the end of the expression specified token (such as a semicolon).
        This is done by iterating until it encounters a token that shouldn't be found in
        an expression.

        :param: end_tokens: tokens that the expression end on. Used to exit early.
        :return: The index of the end of expression.
        """
        index = self._state.get_current()
        valid_expression_tokens = TokenType.valid_expression_types()
        while not self._state.retrieve_token(index).get_token_type() in end_tokens and (self._state.retrieve_token(index).get_token_type() in valid_expression_tokens):
            index += 1
        return index

    def _parse_expression_recursive(self, left_index, right_index):
        """
        Recursively parses an expression within the given token range. Handles precedence and parentheses.

        :param left_index: The left bound of the token range.
        :param right_index: The right bound of the token range.
        :return: The parsed expression node.
        """
        left_token, right_token = self._state.retrieve_token(left_index), self._state.retrieve_token(right_index)
        index_delta = right_index - left_index
        if index_delta == 0:
            token_type = left_token.get_token_type()
            if token_type not in TokenType.valid_expression_types():
                raise SyntaxException(left_token.get_line(), f"Invalid token in expression: {token_type}")
            return self._parser.handle_token(left_index)
        if self._is_nested_parens(left_index, right_index):
            return self._parse_expression_recursive(left_index + 1, right_index - 1)
        operator_precedence = [
            {TokenType.OR},
            {TokenType.AND},
            {TokenType.EQUAL_EQUAL, TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS_EQUAL, TokenType.LESS,
             TokenType.BANG_EQUAL},
            {TokenType.BANG},
            {TokenType.MINUS, TokenType.PLUS},
            {TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULUS},
            {TokenType.EXPONENT},
            {TokenType.FUNCTION_CALL}
        ]
        for operators in operator_precedence:
            index = left_index
            while index < right_index:
                token = self._state.retrieve_token(index)
                if token.is_token_type(TokenType.LEFT_PAREN):
                    index = self._skip_parentheses(index, right_index)
                if token.is_token_type(TokenType.FUNCTION_CALL):
                    expected_index = self._skip_function_call(index, right_index)
                    if expected_index != right_index:
                        index = expected_index
                node = self._handle_by_operations(operators, left_index, right_index, index)
                if node:
                    return node
                index += 1

        raise SyntaxException(
            self._state.retrieve_token(left_index).get_line(),
            "Invalid expression: no valid operations found."
        )

    def _is_nested_parens(self, left_index, right_index):
        """
        Checks if the parentheses between the given left and right indices are nested,
        meaning that the parentheses are part of the same nested group.

        :param left_index: The index of the left parenthesis.
        :param right_index: The index of the right bound for the search.
        :return: `True` if the parentheses are nested, `False` otherwise.
        """
        if not self._within_parens(left_index, right_index):
            return False

        paren_counter, end_index = self._find_parenthesis_count(left_index, right_index)
        return paren_counter == 0 and end_index == right_index

    def _find_parenthesis_count(self, left_index, right_index):
        """
        Scans the tokens between `left_index` and `right_index` to find where a set of parentheses closes
        and the balance of parentheses between the bounds.

        :param left_index: The index of the left parenthesis `'('` where the search begins.
        :param right_index: The index of the right bound for the search.
        :return: A tuple containing:
            - `paren_counter` (int): The final count of parentheses (should be zero if parentheses are balanced).
            - `current_index` (int): The index at which the parentheses balance returns to zero.
        :raises SyntaxException: If there are unmatched left or right parentheses within the given range.
        """
        paren_counter = 0
        current_index = left_index
        while current_index <= right_index:
            token = self._state.retrieve_token(current_index)
            if token.is_token_type(TokenType.LEFT_PAREN):
                paren_counter += 1
            if token.is_token_type(TokenType.RIGHT_PAREN):
                paren_counter -= 1
            if paren_counter == 0:
                break
            current_index += 1

        token_line = self._state.retrieve_token(right_index).get_line()
        if paren_counter > 0:
            raise SyntaxException(token_line, 'Left parenthesis missing closing right.')
        elif paren_counter < 0:
            raise SyntaxException(token_line, 'Right parenthesis missing corresponding left.')
        return paren_counter, current_index

    def _within_parens(self, left_index, right_index):
        """
        Checks if the given tokens are within parentheses.

        :param left_index: The left token index.
        :param right_index: The right token index.
        :return: True if the tokens are within parentheses, False otherwise.
        """
        left_token, right_token = self._state.retrieve_token(left_index), self._state.retrieve_token(right_index)
        return left_token.is_token_type(TokenType.LEFT_PAREN) and right_token.is_token_type(TokenType.RIGHT_PAREN)

    def _skip_parentheses(self, left_index, right_index):
        """
        Skips over a section of tokens enclosed in parentheses.

        :param left_index: The starting index (left parenthesis).
        :param right_index: The ending index.
        :return: The index of the token after the closing parenthesis.
        """
        paren_counter, end_index = self._find_parenthesis_count(left_index, right_index)
        return min(end_index + 1, right_index)

    def _skip_function_call(self, left_index, right_index):
        """
        Skips over a section of tokens that correspond to a function call.

        :param left_index: The starting index (left parenthesis).
        :param right_index: The ending index.
        :return: The index of the token after the closing parenthesis of the function call.
        """
        return self._skip_parentheses(left_index + 2, right_index)

    def _handle_by_operations(self, operations, left_index, right_index, index):
        """
        Handles binary and unary operations based on operator precedence.

        :param operations: Set of operations to process.
        :param left_index: Left bound of the expression.
        :param right_index: Right bound of the expression.
        :param index: Current token index.
        :return: Node representing the operation, or None if no operation was found.
        """
        token = self._state.retrieve_token(index)
        token_type = token.get_token_type()
        if token_type in operations:
            if token_type == TokenType.FUNCTION_CALL:
                return self._handle_function_call(index)
            elif token_type in TokenType.unary_operations():
                return self._handle_unary_operation(index, right_index)
            else:
                return self._handle_binary_operation(left_index, index, right_index)

    def _handle_function_call(self, index):
        """
        Handles parsing function calls in the expression.

        :param index: The index of the unary operator.
        :return: Node representing the function call.
        """
        self._state.set_current(index)
        return self._parser.parse_function_call()

    def _handle_unary_operation(self, index, right_index):
        """
        Handles unary operations (such as negation).

        :param index: The index of the unary operator.
        :param right_index: The right bound of the expression.
        :return: Node representing the unary operation.
        """
        token = self._state.retrieve_token(index)
        right_node = self._parse_expression_recursive(index + 1, right_index)
        if right_node is None:
            raise SyntaxException(token.get_line(), "Invalid expression: missing right operand.")
        context = UnaryOperationContext(right_node)
        return self._parser.handle_token(index, context)

    def _handle_binary_operation(self, left_index, index, right_index):
        """
        Handles binary operations (such as addition, subtraction, etc.).

        :param left_index: Left bound of the left operand.
        :param index: The index of the operator.
        :param right_index: Right bound of the right operand.
        :return: Node representing the binary operation.
        """
        token = self._state.retrieve_token(index)
        left_node = self._parse_expression_recursive(left_index, index - 1)
        if left_node is None:
            raise SyntaxException(token.get_line(), "Invalid expression: missing left operand.")

        right_node = self._parse_expression_recursive(index + 1, right_index)
        if right_node is None:
            raise SyntaxException(token.get_line(), "Invalid expression: missing right operand.")

        context = BinaryOperationContext(left_node, right_node)
        return self._parser.handle_token(index, context)
