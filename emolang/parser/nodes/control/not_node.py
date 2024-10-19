from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class NotNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node, line_number):
        super().__init__(line_number)
        self._condition_node = condition_node

    def evaluate(self, context):
        return not self._condition_node.evaluate(context)

