from abc import ABC, abstractmethod


class AbstractSyntaxTreeNode(ABC):
    @abstractmethod
    def evaluate(self, context):
        pass
