from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class NotNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node):
        self._condition_node = condition_node

    def evaluate(self, context):
        return not self._condition_node.evaluate(context)

