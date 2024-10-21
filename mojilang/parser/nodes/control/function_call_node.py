from mojilang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class FunctionCallNode(AbstractSyntaxTreeNode):
    def __init__(self, function_name, arguments, line_number):
        super().__init__(line_number)
        self._function_name = function_name
        self._arguments = arguments

    def evaluate(self, context):
        function = context.retrieve_variable_value(self._function_name)
        evaluated_args = [argument.evaluate(context) for argument in self._arguments]
        return function.call(context, evaluated_args)
