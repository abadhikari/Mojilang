class ScopeContext:
    """
    Manages both local, parent, and global scopes in the interpreter.

    ScopeContext is responsible for storing and handling variable assignments and lookups.
    It allows for the distinction between local, parent, and global variables
    """

    def __init__(self, block_scope_context, context=None, parent_context=None, global_context=None, ):
        """
        Initializes a new ScopeContext with blockScopeContext, optional local, parent, and global contexts.

        :param block_scope_context: A class responsible for managing the blockScope during parsing or execution.
        :param context: A dictionary representing the local scope of variables. Defaults to an empty dictionary.
        :param parent_context: A dictionary representing the parent scope of variables. Defaults to an empty dictionary.
        :param global_context: A dictionary representing the global scope of identifiers. Defaults to an empty dictionary.
        """
        self._block_scope_context = block_scope_context
        self._local_context = {} if context is None else context
        self._parent_context = parent_context
        self._global_context = {} if global_context is None else global_context

    def assign_value(self, variable_name, value):
        """
        Assigns a value to a variable in the current context.

        :param variable_name: The name of the variable to assign.
        :param value: The value to assign to the variable.
        """
        scope = self._global_context if self._block_scope_context.is_global_scope() else self._local_context
        scope[variable_name] = value

    def reassign_value(self, variable_name, value):
        """
        Reassigns a value to a variable in the current context.

        The method first checks local, then it recursively traverses
        the parent scopes, then finally checks global.

        :param variable_name: The name of the variable to reassign.
        :param value: The value to reassign to the variable.
        """
        if self.local_contains_variable(variable_name):
            self._local_context[variable_name] = value
            return True

        if self._parent_context and self._parent_context.reassign_value(variable_name, value):
            return

        if variable_name in self._global_context:
            self._global_context[variable_name] = value

    def retrieve_variable_value(self, variable_name):
        """
        Retrieves the value of a variable from the scopes.

        The method first checks local, then it recursively traverses
        the parent scopes, then finally checks global.

        :param variable_name: The name of the variable to retrieve.
        :return: The value assigned to the variable.
        """
        if self.local_contains_variable(variable_name):
            return self._local_context[variable_name]

        if self._parent_context:
            return self._parent_context.retrieve_variable_value(variable_name)

        if variable_name in self._global_context:
            return self._global_context[variable_name]

    def local_contains_variable(self, variable_name):
        """
        Checks if a variable is defined in the local scope.

        :param variable_name: The name of the variable to check.
        :return: True if the variable exists in the local scope, False otherwise.
        """
        return variable_name in self._local_context

    def contains_variable(self, variable_name):
        """
        Checks if a variable is defined in the scope.

        :param variable_name: The name of the variable to check.
        :return: True if the variable exists in the local scope, False otherwise.
        """
        return (
            self.local_contains_variable(variable_name)
        ) or (
            self._parent_context.contains_variable(variable_name) if self._parent_context else False
        ) or (
            variable_name in self._global_context
        )

    def create_new_scope_context(self, block_scope):
        """
        Creates a new local ScopeContext that shares the global context with the current one.

        This is used to create a new local scope (such as for function calls) while preserving access to global variables.

        :param block_scope: The block_scope of the new context.
        :return: A new ScopeContext with a separate local scope but shared global context.
        """
        new_block_scope_context = self._block_scope_context.enter_scope(block_scope)
        return ScopeContext(block_scope_context=new_block_scope_context, global_context=self._global_context, parent_context=self)

    def is_block_scope(self, block_scope):
        """Returns if the current block scope is the expected one."""
        return self._block_scope_context.is_block_scope(block_scope)

    def within_block_scope(self, block_scope):
        """Checks if a specific scope type is present in the scope chain."""
        return self._block_scope_context.within_block_scope(block_scope)

    def __repr__(self):
        return f'local_context: {self._local_context}, global_context: {self._global_context}, block_scope_context: {self._block_scope_context}'
