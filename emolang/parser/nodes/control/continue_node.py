from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ContinueNode(AbstractSyntaxTreeNode):
    def __init__(self, line_number):
        super().__init__(line_number)

    def evaluate(self, context):
        return self
