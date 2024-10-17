from emolang.parser.nodes.literal.literal_node import LiteralNode


class NumberLiteralNode(LiteralNode):
    def __init__(self, value):
        super().__init__(value)
