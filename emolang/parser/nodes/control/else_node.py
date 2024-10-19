from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ElseNode(AbstractSyntaxTreeNode):
    def __init__(self, block_node, line_number):
        super().__init__(line_number)
        self._block_node = block_node

    def evaluate(self, context):
        return self._block_node.evaluate(context)
