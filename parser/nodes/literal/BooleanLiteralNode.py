from parser.nodes.literal.LiteralNode import LiteralNode


class BooleanLiteralNode(LiteralNode):
    def __init__(self, value):
        super().__init__(value)
