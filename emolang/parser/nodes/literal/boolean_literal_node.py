from emolang.parser.nodes.literal.literal_node import LiteralNode


class BooleanLiteralNode(LiteralNode):
    def __init__(self, value):
        super().__init__(value)
