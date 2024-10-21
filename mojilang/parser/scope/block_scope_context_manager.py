class BlockScopeContextManager:
    """
    A context manager responsible for entering and exiting a new block scope
    within the current parsing environment.

    Attributes:
        _parser (Parser): The parser instance whose scope is being managed.
        _block_scope_context (BlockScopeContext): The current block scope context that represents the current state of the block hierarchy.
        _new_block_scope (BlockScope): The new block scope to be entered when the context starts (e.g. FUNCTION, LOOP, CONDITIONAL).
    """

    def __init__(self, parser, block_scope_context, new_block_scope):
        """
        Initializes the BlockScopeContextManager with the parser, block_scope_context, and the new block scope.

        :param parser: The current parser instance that manages the scope during parsing.
        :param block_scope_context: The current block scope context representing the block structure at this point.
        :param new_block_scope: The new block scope type to be entered when the context begins (e.g., FUNCTION, LOOP).
        """
        self._parser = parser
        self._block_scope_context = block_scope_context
        self._new_block_scope = new_block_scope

    def __enter__(self):
        """
        Enters the new block scope by creating a new scope context and sets it as the current
        scope in the parser.

        This method is called when the context manager is entered (in a 'with' statement).
        """
        new_block_scope_context = self._block_scope_context.enter_scope(self._new_block_scope)
        self._parser.set_scope(new_block_scope_context)
        return new_block_scope_context

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exits the current block scope and restores the previous scope context.

        This method is called when the context manager is exited (e.g. at the end of a 'with' block).

        :param exc_type: Exception type that occurred in the block.
        :param exc_value: Exception value that occurred in the block.
        :param traceback: Traceback object for the exception.
        """
        self._parser.set_scope(self._block_scope_context)
