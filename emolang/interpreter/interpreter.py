class Interpreter:
    def __init__(self, abstract_syntax_tree):
        self._abstract_syntax_tree = abstract_syntax_tree
        self._context = {}

    def execute(self):
        self._abstract_syntax_tree.evaluate(self._context)
