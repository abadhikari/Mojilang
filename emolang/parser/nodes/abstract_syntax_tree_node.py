from abc import ABC, abstractmethod


class AbstractSyntaxTreeNode(ABC):
    def __init__(self, line_number):
        self._line_number = line_number

    @abstractmethod
    def evaluate(self, context):
        pass

    def get_line_number(self):
        return self._line_number
