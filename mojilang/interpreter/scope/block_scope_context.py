from mojilang.interpreter.scope.block_scope import BlockScope


class BlockScopeContext:
    """
    A class responsible for managing the blockScope during parsing or execution.

    Each BlockScope represents a block of code (function, loop, or conditional) that may contain
    its own identifiers.

    Attributes:
        _block_scope the active block scope.
        _parent_scope (BlockScopeContext): The parent scope of the current block, representing the outer block.
    """
    def __init__(self, block_scope, parent_scope=None):
        """
        Initializes a new BlockScopeContext with a block scope and an optional parent scope.

        :param block_scope: The type of block scope (e.g. BlockScope.LOOP).
        :param parent_scope: The parent BlockScopeContext representing the enclosing scope.
        """
        self._block_scope = block_scope
        self._parent_scope = parent_scope

    def enter_scope(self, new_block_scope):
        """
        Enters a new block scope by creating a new (child) BlockScopeContext.

        :param new_block_scope: The type of the new block scope being entered (e.g. BlockScope.LOOP).
        :return: A new BlockScopeContext representing the entered scope, with the current scope as the parent.
        """
        return BlockScopeContext(new_block_scope, self)

    def current_block_scope(self):
        """Returns the current block scope."""
        return self._block_scope

    def is_block_scope(self, block_scope):
        """Returns if the current block scope is the expected one."""
        return self.current_block_scope() == block_scope

    def is_global_scope(self):
        """Returns if the current block scope is global scope."""
        return self.is_block_scope(BlockScope.GLOBAL)

    def is_function_scope(self):
        """Returns if the current block scope is function scope."""
        return self.is_block_scope(BlockScope.FUNCTION)

    def within_block_scope(self, block_scope):
        """
        Checks if a specific scope type is present in the scope chain.

        This method can be used to verify whether a certain block scope (e.g. a loop)
        is currently active within the nested block structure.

        :param block_scope: The type of scope to check for (e.g. BlockScope.LOOP).
        :return: True if the scope type is in the chain, False otherwise.
        """
        return block_scope == self._block_scope or (self._parent_scope.within_block_scope(block_scope) if self._parent_scope else False)

    def __repr__(self):
        return f'block_scope: {self._block_scope}'
