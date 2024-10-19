from mojilang.lexer import TokenType
from mojilang.parser.nodes import (
    AdditionNode,
    MultiplicationNode,
    SubtractionNode,
    ModulusNode,
    DivisionNode,
    ExponentNode,
    AndNode,
    EqualsNode,
    GreaterNode,
    GreaterEqualsNode,
    LessNode,
    LessEqualsNode,
    NotNode,
    NotEqualsNode,
    OrNode,
)


class OperationParser:
    """
    The OperationParser class is responsible for parsing binary and unary operations in expressions.

    This class focuses on parsing operations like addition, subtraction, multiplication, division,
    logical comparisons, and boolean logic, converting them into appropriate AST nodes.
    """

    def parse(self, token, context):
        """
        Parses an operation token and returns the appropriate operation node based on the context.

        :param token: The operation token to parse.
        :param context: The context (unary or binary) in which the operation occurs.
        :return: The corresponding operation node.
        """
        binary_operation_map = {
            TokenType.AND: AndNode,
            TokenType.BANG_EQUAL: NotEqualsNode,
            TokenType.DIVIDE: DivisionNode,
            TokenType.EQUAL_EQUAL: EqualsNode,
            TokenType.EXPONENT: ExponentNode,
            TokenType.GREATER: GreaterNode,
            TokenType.GREATER_EQUAL: GreaterEqualsNode,
            TokenType.LESS: LessNode,
            TokenType.LESS_EQUAL: LessEqualsNode,
            TokenType.MINUS: SubtractionNode,
            TokenType.MODULUS: ModulusNode,
            TokenType.MULTIPLY: MultiplicationNode,
            TokenType.OR: OrNode,
            TokenType.PLUS: AdditionNode,
        }
        token_type = token.get_token_type()
        line_number = token.get_line()
        if token_type in binary_operation_map:
            operation_class = binary_operation_map[token_type]
            left_operand, right_operand = context.get_left_operand(), context.get_right_operand()
            return operation_class(left_operand, right_operand, line_number)

        if token.is_token_type(TokenType.BANG):
            return NotNode(context.get_operand(), line_number)
