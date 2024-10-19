from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class InputNode(AbstractSyntaxTreeNode):
    def __init__(self, input_message, line_number):
        super().__init__(line_number)
        self._input_message = input_message

    def evaluate(self, context):
        return input(self._input_message)
