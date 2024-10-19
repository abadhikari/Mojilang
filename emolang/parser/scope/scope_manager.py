class ScopeManager:
    """
    A context manager responsible for entering and exiting a new scope
    within the current parsing environment.

    Attributes:
        _scope (Scope): The current Scope instance managing the scope stack.
        _new_block_scope (BlockScope): The new block scope to be entered when the context starts.
    """

    def __init__(self, scope, new_block_scope):
        """
        Initializes the ScopeManager with the current scope and the new block scope to enter.

        :param scope: The current Scope instance that manages the scope.
        :param new_block_scope: The new block scope type to be entered when the context begins.
        """
        self._scope = scope
        self._new_block_scope = new_block_scope

    def __enter__(self):
        """
        Enters the new block scope by pushing it onto the scope stack.

        This method is called when the context manager is entered (in a 'with' statement).
        It updates the Scope instance by adding the new block scope.
        """
        self._scope.enter_scope(self._new_block_scope)

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exits the current block scope by popping it off the scope stack.

        This method is called when the context manager is exited (e.g., when the 'with' block ends).
        It ensures the current block scope is removed from the Scope instance.

        :param exc_type: Exception type that occurred in the block.
        :param exc_value: Exception value that occurred in the block.
        :param traceback: Traceback object for the exception.
        """
        self._scope.exit_scope()
