from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.control.return_value import ReturnValue


class ReturnNode(AbstractSyntaxTreeNode):
    def __init__(self, return_value_node, line_number):
        super().__init__(line_number)
        self._return_value_node = return_value_node

    def evaluate(self, context):
        return ReturnValue(self._return_value_node.evaluate(context))
