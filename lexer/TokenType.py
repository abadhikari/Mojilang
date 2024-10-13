from enum import Enum


class TokenType(Enum):
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
    def valid_print_types(cls):
        return {cls.NUMBER, cls.STRING, cls.IDENTIFIER}

    @classmethod
    def valid_assignment_types(cls):
        return {cls.NUMBER, cls.STRING, cls.IDENTIFIER}

    @classmethod
    def operation_types(cls):
        return {cls.MULTIPLY, cls.DIVIDE, cls.PLUS, cls.MINUS, cls.MODULUS, cls.EXPONENT}
