from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from emolang.parser.nodes.callable import Callable


class FunctionNode(AbstractSyntaxTreeNode, Callable):
    def __init__(self, function_block_node):
        self._function_block_node = function_block_node

    def evaluate(self, context):
        self._function_block_node.evaluate(context)

    def call(self, context, arguments):
        pass
