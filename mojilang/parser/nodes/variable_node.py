from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.lexer import SyntaxException


class VariableNode(AbstractSyntaxTreeNode):
    def __init__(self, name, line_number):
        super().__init__(line_number)
        self._name = name

    def evaluate(self, context):
        if not context.contains_variable(self._name):
            raise SyntaxException(self._line_number, f"Undefined variable '{self._name}'")
        return context.retrieve_variable_value(self._name)

    def get_name(self):
        return self._name
