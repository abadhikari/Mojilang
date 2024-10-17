from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class LiteralNode(AbstractSyntaxTreeNode):
    def __init__(self, value):
        self._value = value

    def evaluate(self, context):
        return self._value

    def __repr__(self):
        return str(self._value)
