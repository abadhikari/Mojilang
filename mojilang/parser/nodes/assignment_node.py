from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.runtime_exception import RuntimeException


class AssignmentNode(AbstractSyntaxTreeNode):
    def __init__(self, variable_node, value_node, line_number):
        super().__init__(line_number)
        self._variable_node = variable_node
        self._value_node = value_node

    def evaluate(self, context):
        new_value = self._value_node.evaluate(context)
        variable_name = self._variable_node.get_name()
        if context.contains_variable(variable_name):
            raise RuntimeException("Variable has already been declared. Cannot redeclare.", self.get_line_number())
        context.assign_value(self._variable_node.get_name(), new_value)

    def get_variable_node(self):
        return self._variable_node

    def get_value_node(self):
        return self._value_node
