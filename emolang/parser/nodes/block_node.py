from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from .return_node import ReturnNode


class BlockNode(AbstractSyntaxTreeNode):
    def __init__(self, nodes, line_number):
        super().__init__(line_number)
        self._nodes = nodes

    def evaluate(self, context):
        return_value = None
        for node in self._nodes:
            return_value = node.evaluate(context)
            if isinstance(node, ReturnNode):
                return return_value
        return return_value

    def get_nodes(self):
        return self._nodes
