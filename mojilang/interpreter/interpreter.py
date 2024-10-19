from mojilang.interpreter.scope_context import ScopeContext


class Interpreter:
    """
    The Interpreter class is responsible for executing the Abstract Syntax Tree (AST).
    It takes an AST, processes it, and evaluates the expressions and operations defined within.
    The interpreter uses a context (a dictionary) to store variable values during execution.
    """

    def __init__(self, abstract_syntax_tree):
        """
        Initializes the Interpreter with an Abstract Syntax Tree (AST).

        :param abstract_syntax_tree: The AST to be executed. This represents the parsed structure of the program.
        """
        self._abstract_syntax_tree = abstract_syntax_tree
        self._context = ScopeContext()

    def execute(self):
        """
        Executes the program by evaluating the Abstract Syntax Tree (AST).
        The AST is evaluated in the context of the interpreter's state, which stores variables and their values.

        :return: 0 if execution is successful, raises an error if execution fails.
        """
        try:
            self._abstract_syntax_tree.evaluate(self._context)
            return 0
        except Exception as e:
            raise RuntimeError(f"Execution error: {e}")
