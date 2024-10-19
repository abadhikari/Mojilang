from emolang.parser.nodes.abstract_syntax_tree_node import AbstractSyntaxTreeNode


class ConditionalNode(AbstractSyntaxTreeNode):
    """
    Represents conditional control flow in the abstract syntax tree (AST) for EmoLang.

    This node handles 'if' and 'elseif' logic in conditional statements. It evaluates
    a condition and, if true, executes a corresponding block of code. If the condition is false,
    it delegates evaluation to the next conditional node, if it's present.
    """

    def __init__(self, condition_node, block_node, next_conditional_node, line_number):
        """
        Initializes the ConditionalNode.

        :param condition_node: The condition node to evaluate.
        :param block_node: The block of code to execute if the condition is true.
        :param next_conditional_node: The next node in the chain (for 'elif' or 'else'). None if this is the final node.
        """
        super().__init__(line_number)
        self._condition_node = condition_node
        self._block_node = block_node
        self._next_conditional_node = next_conditional_node

    def evaluate(self, context):
        """
        Evaluates the condition and executes the block if true, otherwise evaluates the next conditional node.

        :param context: The current execution context in which the condition and block are evaluated.
        :return: The result of evaluating the block if the condition is true, or the result of the next
                 conditional node's evaluation if the condition is false. Returns None if no conditions match.
        """
        if self._condition_node.evaluate(context):
            return self._block_node.evaluate(context)
        else:
            if self._next_conditional_node:
                return self._next_conditional_node.evaluate(context)
