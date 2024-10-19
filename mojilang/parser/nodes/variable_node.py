from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class VariableNode(AbstractSyntaxTreeNode):
    def __init__(self, name, line_number):
        super().__init__(line_number)
        self._name = name

    def evaluate(self, context):
        return context.retrieve_variable_value(self._name)

    def get_name(self):
        return self._name
