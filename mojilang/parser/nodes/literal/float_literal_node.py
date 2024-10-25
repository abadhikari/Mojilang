from mojilang.parser.nodes.literal.number_literal_node import NumberLiteralNode


class FloatLiteralNode(NumberLiteralNode):
    def __init__(self, value, line_number):
        super().__init__(value, line_number)