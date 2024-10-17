from parser.nodes.operation.OperationNode import OperationNode


class AndNode(OperationNode):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand, 'and')

    def evaluate(self, context):
        left_value = self.get_left_operand().evaluate(context)
        right_value = self.get_right_operand().evaluate(context)
        return left_value and right_value