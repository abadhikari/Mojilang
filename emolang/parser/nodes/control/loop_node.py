from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class LoopNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node, block_node, line_number):
        super().__init__(line_number)
        self._condition_node = condition_node
        self._block_node = block_node

    def evaluate(self, context):
        value = None
        while self._condition_node.evaluate(context):
            value = self._block_node.evaluate(context)
        return value
