from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.control.break_node import BreakNode
from mojilang.parser.nodes.control.continue_node import ContinueNode
from mojilang.interpreter.scope import BlockScope
from mojilang.parser.nodes.control.return_value import ReturnValue
from mojilang.parser.runtime_exception import RuntimeException


class BlockNode(AbstractSyntaxTreeNode):
    def __init__(self, nodes, line_number):
        super().__init__(line_number)
        self._nodes = nodes

    def evaluate(self, context):
        return_value = None
        for node in self._nodes:
            return_value = node.evaluate(context)
            if isinstance(return_value, ReturnValue):
                if not context.within_block_scope(BlockScope.FUNCTION):
                    raise RuntimeException("'return' outside of function.", node.get_line_number())
                return return_value
            if (isinstance(return_value, BreakNode) or isinstance(return_value, ContinueNode)) and context.within_block_scope(BlockScope.LOOP):
                return return_value
        return return_value

    def get_nodes(self):
        return self._nodes
