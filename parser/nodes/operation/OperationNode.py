from abc import abstractmethod
from parser.nodes.AbstractSyntaxTreeNode import AbstractSyntaxTreeNode


class OperationNode(AbstractSyntaxTreeNode):
    def __init__(self, left_operand, right_operand):
        self._left_operand = left_operand
        self._right_operand = right_operand

    @abstractmethod
    def evaluate(self, context):
        pass

    def get_left_operand(self):
        return self._left_operand

    def get_right_operand(self):
        return self._right_operand
