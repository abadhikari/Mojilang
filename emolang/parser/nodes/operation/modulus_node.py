from emolang.parser.nodes.operation.operation_node import OperationNode


class ModulusNode(OperationNode):
    def __init__(self, left_operand, right_operand):
        super().__init__(left_operand, right_operand, '%')

    def evaluate(self, context):
        left_value = self.get_left_operand().evaluate(context)
        right_value = self.get_right_operand().evaluate(context)
        return left_value % right_value
