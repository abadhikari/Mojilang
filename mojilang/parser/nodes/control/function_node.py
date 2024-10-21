from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.callable import Callable


class FunctionNode(AbstractSyntaxTreeNode, Callable):
    def __init__(self, function_name, argument_names, function_block_node, line_number):
        super().__init__(line_number)
        self._function_name = function_name
        self._argument_names = argument_names
        self._function_block_node = function_block_node

    def evaluate(self, context):
        context.assign_value(self._function_name, self)

    def call(self, context, arguments):
        for arg_name, arg_value in zip(self._argument_names, arguments):
            context.assign_value(arg_name, arg_value)
        return self._function_block_node.evaluate(context)
