from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class LiteralNode(AbstractSyntaxTreeNode):
    def __init__(self, value, line_number):
        super().__init__(line_number)
        self._value = value

    def evaluate(self, context):
        return self._value

    def __repr__(self):
        return str(self._value)
