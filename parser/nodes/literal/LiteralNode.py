from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class LiteralNode(AbstractSyntaxTreeNode):
    def __init__(self, value):
        self._value = value

    def evaluate(self, context):
        return self._value

    def __repr__(self):
        return str(self._value)
