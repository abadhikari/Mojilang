from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class PrintNode(AbstractSyntaxTreeNode):
    def __init__(self, node_to_print, line_number):
        super().__init__(line_number)
        self._node_to_print = node_to_print

    def evaluate(self, context):
        value_to_print = self._node_to_print.evaluate(context)
        if isinstance(value_to_print, bool):
            value_to_print = "😤" if value_to_print else "😔"
        print(value_to_print)

    def get_node_to_print(self):
        return self._node_to_print
