from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ElseNode(AbstractSyntaxTreeNode):
    def __init__(self, block_node):
        self._block_node = block_node

    def evaluate(self, context):
        return self._block_node.evaluate(context)
