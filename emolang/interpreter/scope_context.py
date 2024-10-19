class ScopeContext:
    """
    Manages both local variable and global scopes in the interpreter.

    ScopeContext is responsible for storing and handling variable assignments and lookups.
    It allows for the distinction between local (function or block) variables and global
    identifiers (functions, classes, etc.).

    Attributes:
        _context (dict): A dictionary representing the local scope of variables.
        _global_context (dict): A dictionary representing the global scope of identifiers.
    """
    def __init__(self, context=None, global_context=None):
        """
        Initializes a new ScopeContext with optional local and global contexts.

        :param context: A dictionary representing the local scope of variables. Defaults to an empty dictionary.
        :param global_context: A dictionary representing the global scope of identifiers. Defaults to an empty dictionary.
        """
        self._context = context if context else {}
        self._global_context = global_context if global_context else {}

    def assign_value(self, variable_name, value):
        """
        Assigns a value to a local variable in the current context.

        :param variable_name: The name of the variable to assign.
        :param value: The value to assign to the variable.
        """
        self._context[variable_name] = value

    def retrieve_variable_value(self, variable_name):
        """
        Retrieves the value of a variable from the local context.

        :param variable_name: The name of the variable to retrieve.
        :return: The value assigned to the variable.
        """
        return self._context[variable_name]

    def contains_variable(self, variable_name):
        """
        Checks if a variable is defined in the local context.

        :param variable_name: The name of the variable to check.
        :return: True if the variable exists in the local context, False otherwise.
        """
        return variable_name in self._context

    def assign_global_value(self, identifier, value):
        """
        Assigns a value to a global identifier in the global context.

        :param identifier: The name of the global identifier to assign.
        :param value: The value to assign to the global identifier.
        """
        self._context[identifier] = value

    def retrieve_global_identifier(self, identifier):
        """
        Retrieves the value of a global identifier from the global context.

        :param identifier: The name of the global identifier to retrieve.
        :return: The value assigned to the global identifier.
        :raises KeyError: If the global identifier is not found in the global context.
        """
        return self._global_context[identifier]

    def contains_global_identifier(self, identifier):
        """
        Checks if a global identifier is defined in the global context.

        :param identifier: The name of the global identifier to check.
        :return: True if the global identifier exists in the global context, False otherwise.
        """
        return identifier in self._global_context

    def create_new_context(self):
        """
        Creates a new local ScopeContext that shares the global context with the current one.

        This is used to create a new local scope (such as for function calls) while preserving access to global variables.

        :return: A new ScopeContext with a separate local scope but shared global context.
        """
        return ScopeContext(global_context=self._global_context)
