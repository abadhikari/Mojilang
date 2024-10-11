from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class AssignmentNode(AbstractSyntaxTreeNode):
    def __init__(self, variable_node, value_node):
        self._variable_node = variable_node
        self._value_node = value_node

    def evaluate(self, context):
        new_value = self._value_node.evaluate(context)
        context[self._variable_node.get_name()] = new_value
