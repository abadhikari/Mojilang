from abc import abstractmethod
from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class OperationNode(AbstractSyntaxTreeNode):
    def __init__(self, left_operand, right_operand, value):
        self._left_operand = left_operand
        self._right_operand = right_operand
        self.value = value

    @abstractmethod
    def evaluate(self, context):
        pass

    def get_left_operand(self):
        return self._left_operand

    def get_right_operand(self):
        return self._right_operand