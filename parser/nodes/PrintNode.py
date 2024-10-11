from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class PrintNode(AbstractSyntaxTreeNode):
    def __init__(self, node_to_print):
        self._node_to_print = node_to_print

    def evaluate(self, context):
        value_to_print = self._node_to_print.evaluate(context)
        print(value_to_print)
