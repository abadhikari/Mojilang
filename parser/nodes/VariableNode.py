from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class VariableNode(AbstractSyntaxTreeNode):
    def __init__(self, name):
        self._name = name

    def evaluate(self, context):
        return context[self._name]

    def get_name(self):
        return self._name
