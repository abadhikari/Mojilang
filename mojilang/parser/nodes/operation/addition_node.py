from mojilang.parser.nodes.operation.operation_node import OperationNode


class AdditionNode(OperationNode):
    def __init__(self, left_operand, right_operand, line_number):
        super().__init__(left_operand, right_operand, '+', line_number)

    def evaluate(self, context):
        left_value = self.get_left_operand().evaluate(context)
        right_value = self.get_right_operand().evaluate(context)
        return left_value + right_value
