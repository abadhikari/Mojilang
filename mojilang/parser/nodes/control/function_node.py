from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode
from mojilang.parser.nodes.callable import Callable
from mojilang.parser.nodes.control.return_value import ReturnValue


class FunctionNode(AbstractSyntaxTreeNode, Callable):
    def __init__(self, function_name, argument_names, function_block_node, line_number):
        super().__init__(line_number)
        self._function_name = function_name
        self._argument_names = argument_names
        self._function_block_node = function_block_node

    def evaluate(self, context):
        context.assign_value(self._function_name, self)

    def call(self, context, argument_values):
        arguments = zip(self._argument_names, argument_values)
        for arg_name, arg_value in arguments:
            context.assign_value(arg_name, arg_value)

        return_value = self._function_block_node.evaluate(context)
        return return_value.get_value() if isinstance(return_value, ReturnValue) else return_value
