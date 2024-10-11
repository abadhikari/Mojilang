from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class InputNode(AbstractSyntaxTreeNode):
    def __init__(self, input_message):
        self._input_message = input_message

    def evaluate(self, context):
        return input(self._input_message)
