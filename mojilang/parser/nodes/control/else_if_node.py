from mojilang.parser.nodes.control.conditional_node import ConditionalNode


class ElseIfNode(ConditionalNode):
    def __init__(self, condition_node, block_node, next_conditional_node, line_number):
        super().__init__(condition_node, block_node, next_conditional_node, line_number)
