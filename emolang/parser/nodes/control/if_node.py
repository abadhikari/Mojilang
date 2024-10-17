from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class IfNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node, if_block_node, else_block_node):
        self._condition_node = condition_node
        self._if_block_node = if_block_node
        self._else_block_node = else_block_node

    def evaluate(self, context):
        if self._condition_node.evaluate(context):
            return self._if_block_node.evaluate(context)
        else:
            return self._else_block_node.evaluate(context)
