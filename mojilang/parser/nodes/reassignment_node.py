from mojilang.parser.nodes.assignment_node import AssignmentNode
from mojilang.parser.runtime_exception import RuntimeException


class ReassignmentNode(AssignmentNode):
    def __init__(self, variable_node, value_node, line_number):
        super().__init__(variable_node, value_node, line_number)

    def evaluate(self, context):
        new_value = self._value_node.evaluate(context)
        variable_name = self._variable_node.get_name()
        if not context.current_scope_contains_variable(variable_name):
            raise RuntimeException("Variable has not been declared yet.", self.get_line_number())
        context.reassign_value(self._variable_node.get_name(), new_value)
