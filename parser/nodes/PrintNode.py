from parser.nodes.literal import BooleanLiteralNode
from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class PrintNode(AbstractSyntaxTreeNode):
    def __init__(self, node_to_print):
        self._node_to_print = node_to_print

    def evaluate(self, context):
        value_to_print = self._node_to_print.evaluate(context)
        if isinstance(value_to_print, bool):
            value_to_print = "😤" if value_to_print else "😔"
        print(value_to_print)
