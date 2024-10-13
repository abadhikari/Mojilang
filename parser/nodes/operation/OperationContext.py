class OperationContext:
    def __init__(self, left_operand, right_operand):
        self._left_operand = left_operand
        self._right_operand = right_operand

    def get_left_operand(self):
        return self._left_operand

    def get_right_operand(self):
        return self._right_operand
