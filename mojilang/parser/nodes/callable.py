from abc import ABC, abstractmethod


class Callable(ABC):
    @abstractmethod
    def call(self, context, arguments):
        pass
