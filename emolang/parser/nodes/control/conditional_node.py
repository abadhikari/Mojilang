from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ConditionalNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node, block_node, next_conditional_node):
        self._condition_node = condition_node
        self._block_node = block_node
        self._next_conditional_node = next_conditional_node

    def evaluate(self, context):
        if self._condition_node.evaluate(context):
            return self._block_node.evaluate(context)
        else:
            if self._next_conditional_node:
                return self._next_conditional_node.evaluate(context)

    def set_next_conditional_node(self, next_conditional_node):
        self._next_conditional_node = next_conditional_node
