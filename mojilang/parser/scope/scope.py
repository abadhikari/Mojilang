import copy


class Scope:
    """
    A class responsible for managing the scope during parsing or execution.

    Each scope represents a block of code (function, loop, or conditional) that may contain
    its own identifiers (variables, symbols, etc.).

    Attributes:
        _block_scope_stack (list): A stack (list) that holds the active block scopes.
    """
    def __init__(self):
        """
        Initializes an empty scope stack.

        The stack will contain different block scopes (loop, function, etc.)
        as the program enters and exits blocks of code.
        """
        self._block_scope_stack = []

    def enter_scope(self, new_scope):
        """
        Pushes a new scope onto the scope stack.

        This method is called when entering a new block of code (e.g. a function or loop).

        :param new_scope: The type of the new block scope being entered (e.g. BlockScope.LOOP).
        """
        self._block_scope_stack.append(new_scope)

    def exit_scope(self):
        """
        Pops the current scope off the scope stack.

        This method is called when exiting the current block of code (e.g. leaving a function or loop).
        """
        if self._block_scope_stack:
            self._block_scope_stack.pop()

    def current_scope(self):
        """
        Returns the current scope (the top of the stack).

        This method returns the most recently entered scope, which represents
        the current active block of code.

        :return: The current block scope, or None if no scopes are present.
        """
        return self._block_scope_stack[-1] if self._block_scope_stack else None

    def within_block_scope(self, scope_type):
        """
        Checks if a specific scope type is present in the scope stack.

        This method can be used to verify whether a certain block scope (e.g. a loop)
        is currently active within the nested block structure.

        :param scope_type: The type of scope to check for (e.g. BlockScope.LOOP).
        :return: True if the scope type is in the stack, False otherwise.
        """
        return scope_type in self._block_scope_stack

    def create_copy(self):
        """
        Creates a deep copy of the current Scope instance.

        This method is used to preserve the current state of the scope stack when passing
        the scope to nodes as a sort of snapshot during interpreter execution.

        :return: A deep copy of the Scope instance, including its scope stack.
        """
        return copy.deepcopy(self)
