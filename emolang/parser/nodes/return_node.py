from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ReturnNode(AbstractSyntaxTreeNode):
    def __init__(self, return_value_node, line_number):
        super().__init__(line_number)
        self._return_value_node = return_value_node

    def evaluate(self, context):
        return self._return_value_node.evaluate(context)
