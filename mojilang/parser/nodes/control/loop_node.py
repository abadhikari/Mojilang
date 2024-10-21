from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.control.break_node import BreakNode
from mojilang.parser.nodes.control.continue_node import ContinueNode


class LoopNode(AbstractSyntaxTreeNode):
    def __init__(self, condition_node, block_node, line_number):
        super().__init__(line_number)
        self._condition_node = condition_node
        self._block_node = block_node

    def evaluate(self, context):
        value = None
        while self._condition_node.evaluate(context):
            new_context = context.create_new_scope_context()
            value = self._block_node.evaluate(new_context)
            if isinstance(value, BreakNode):
                break
            if isinstance(value, ContinueNode):
                continue
        return value
