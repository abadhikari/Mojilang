from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class ReturnNode(AbstractSyntaxTreeNode):
    def __init__(self, return_value_node):
        self._return_value_node = return_value_node

    def evaluate(self, context):
        return self._return_value_node.evaluate(context)
