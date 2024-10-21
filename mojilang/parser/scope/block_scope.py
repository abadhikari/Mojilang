from enum import Enum


class BlockScope(Enum):
    """
    Enum representing different types of block scopes in the Mojilang interpreter.

    This Enum is used to differentiate between various contexts or scopes in the interpreter,
    such as functions, loops, conditionals, and the global scope. The block scope helps
    in managing variable visibility and execution flow within specific blocks of code.

    Attributes:
        FUNCTION (str): Represents the scope of a function block.
        LOOP (str): Represents the scope of a loop block (e.g., for or while).
        CONDITIONAL (str): Represents the scope of a conditional block (e.g., if statements).
        GLOBAL (str): Represents the global scope, which is accessible throughout the entire program.
    """
    FUNCTION = "FUNCTION"
    LOOP = "LOOP"
    CONDITIONAL = "CONDITIONAL"
    GLOBAL = "GLOBAL"
