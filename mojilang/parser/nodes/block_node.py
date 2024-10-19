from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.return_node import ReturnNode
from mojilang.parser.nodes.control.break_node import BreakNode
from mojilang.parser.nodes.control.continue_node import ContinueNode
from mojilang.parser.nodes.block_scope import BlockScope


class BlockNode(AbstractSyntaxTreeNode):
    def __init__(self, nodes, scope, line_number):
        super().__init__(line_number)
        self._nodes = nodes
        self._scope = scope

    def evaluate(self, context):
        return_value = None
        for node in self._nodes:
            return_value = node.evaluate(context)
            if isinstance(node, ReturnNode):
                return return_value
            if (isinstance(return_value, BreakNode) or isinstance(return_value, ContinueNode)) and self._scope.within_block_scope(BlockScope.LOOP):
                return return_value
        return return_value

    def get_nodes(self):
        return self._nodes

    def get_scope(self):
        return self._scope
