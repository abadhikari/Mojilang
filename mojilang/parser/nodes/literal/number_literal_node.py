from mojilang.parser.nodes.literal.literal_node import LiteralNode


class NumberLiteralNode(LiteralNode):
    def __init__(self, value, line_number):
        super().__init__(value, line_number)
