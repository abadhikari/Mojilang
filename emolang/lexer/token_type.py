from enum import Enum


class TokenType(Enum):
    """
    The TokenType Enum defines all possible token types in EmoLang.

    These include single-character tokens (such as parentheses, braces, and operators),
    multi-character tokens (such as comparison operators), literals (like numbers and strings),
    and keywords (such as 'if', 'loop', 'print', etc.).
    Each token type is represented by a string name that corresponds to the type of token.
    """

    # Single character tokens
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    SEMI_COLON = 'SEMI_COLON'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    MODULUS = 'MODULUS'
    EXPONENT = 'EXPONENT'

    # One or two character tokens
    BANG = 'BANG'
    BANG_EQUAL = 'BANG_EQUAL'
    EQUAL = 'EQUAL'
    EQUAL_EQUAL = 'EQUAL_EQUAL'
    GREATER = 'GREATER'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS = 'LESS'
    LESS_EQUAL = 'LESS_EQUAL'

    # Literals
    IDENTIFIER = 'IDENTIFIER'
    STRING = 'STRING'
    NUMBER = 'NUMBER'

    # Keywords
    AND = 'AND'
    ELSE = 'ELSE'
    FALSE = 'FALSE'
    LOOP = 'LOOP'
    IF = 'IF'
    OR = 'OR'
    PRINT = 'PRINT'
    INPUT = 'INPUT'
    RETURN = 'RETURN'
    TRUE = 'TRUE'
    VAR = 'VAR'
    FUNCTION = 'FUNCTION'

    EOF = 'EOF'

    @classmethod
    def literal_types(cls):
        """
        Returns a set of token types that represent literal values in EmoLang.

        :return: A set containing NUMBER, STRING, TRUE, and FALSE token types.
        """
        return {cls.NUMBER, cls.STRING, cls.TRUE, cls.FALSE}

    @classmethod
    def valid_print_types(cls):
        """
        Returns a set of token types that are valid for print statements in EmoLang.
        This includes identifiers and literal types.

        :return: A set containing IDENTIFIER and all literal token types.
        """
        return {cls.IDENTIFIER} | cls.literal_types()

    @classmethod
    def operation_types(cls):
        """
        Returns a set of token types that represent valid operations in EmoLang.
        These include arithmetic operators, comparison operators, and logical operators.

        :return: A set of token types representing valid operations.
        """
        return {cls.MULTIPLY, cls.DIVIDE, cls.PLUS, cls.MINUS, cls.MODULUS, cls.EXPONENT, cls.BANG, cls.BANG_EQUAL, cls.EQUAL_EQUAL, cls.LESS, cls.LESS_EQUAL, cls.GREATER, cls.GREATER_EQUAL, cls.AND, cls.OR}

    @classmethod
    def unary_operations(cls):
        """
        Returns a set of token types that represent valid unary operations in EmoLang.
        Unary operations operate on a single operand (e.g., logical negation).

        :return: A set containing unary operators.
        """
        return {cls.BANG}

    @classmethod
    def valid_expression_types(cls):
        """
        Returns a set of token types that are valid within an expression in EmoLang.
        This includes valid print types, operations, and parentheses.

        :return: A set containing valid token types for expressions.
        """
        return cls.valid_print_types() | cls.operation_types() | {cls.LEFT_PAREN, cls.RIGHT_PAREN}
