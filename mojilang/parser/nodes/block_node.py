from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.return_node import ReturnNode
from mojilang.parser.nodes.control.break_node import BreakNode
from mojilang.parser.nodes.control.continue_node import ContinueNode
from mojilang.parser.scope.block_scope import BlockScope


class BlockNode(AbstractSyntaxTreeNode):
    def __init__(self, nodes, block_scope_context, line_number):
        super().__init__(line_number)
        self._nodes = nodes
        self._block_scope_context = block_scope_context

    def evaluate(self, context):
        previous_block_scope_context = context.update_block_scope_context(self._block_scope_context)
        new_context = self._handle_context(context)
        try:
            return_value = None
            for node in self._nodes:
                return_value = node.evaluate(new_context)
                if isinstance(node, ReturnNode):
                    return return_value
                if (isinstance(return_value, BreakNode) or isinstance(return_value, ContinueNode)) and self._block_scope_context.within_block_scope(BlockScope.LOOP):
                    return return_value
            return return_value
        finally:
            context.update_block_scope_context(previous_block_scope_context)

    def _handle_context(self, context):
        return context if context.is_block_scope(BlockScope.LOOP) or context.is_block_scope(BlockScope.GLOBAL) else context.create_new_scope_context()

    def get_nodes(self):
        return self._nodes

    def get_scope(self):
        return self._block_scope_context
