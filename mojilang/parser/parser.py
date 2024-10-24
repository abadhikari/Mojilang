from mojilang.lexer import TokenType, SyntaxException
from mojilang.parser.nodes import (
    AssignmentNode,
    IfNode,
    ElseIfNode,
    ElseNode,
    BlockNode,
    NumberLiteralNode,
    PrintNode,
    StringLiteralNode,
    VariableNode,
    BooleanLiteralNode,
    ReassignmentNode,
    LoopNode,
    BreakNode,
    ContinueNode,
    FunctionNode,
    ReturnNode,
    FunctionCallNode
)
from mojilang.parser.parser_state import ParserState
from mojilang.parser.expression_parser import ExpressionParser
from mojilang.parser.operation_parser import OperationParser


class Parser:
    """
    The Parser class is responsible for transforming a list of tokens into an Abstract Syntax Tree (AST).
    It handles parsing variable assignments, expressions, operations, and print statements.
    The algorithm used here to construct the AST is recursive descent parsing.
    """

    def __init__(self, tokens):
        """
        Initializes the parser with a list of tokens.

        :param tokens: The list of tokens generated by the lexer.
        """
        self._state = ParserState(tokens)
        self._expression_parser = ExpressionParser(self)
        self._operation_parser = OperationParser()

    def parse(self):
        """
        The main entry point for parsing. It loops through the tokens and parses each one,
        generating a BlockNode (AST root) containing all parsed nodes.

        :return: BlockNode representing the entire parsed program.
        """
        line_number = self._state.current_line_number()
        nodes = []
        while self._state.in_bounds(self._state.get_current()) and not self._state.is_eof_token():
            node = self.handle_token()
            nodes.append(node)
        return BlockNode(nodes, line_number)

    def handle_token(self, index=None, context=None):
        """
        Handles a token based on its type. This function delegates token-specific logic to
        different parsing methods (e.g., print, identifier, variable).

        :param index: The current token index (defaults to _current).
        :param context: Context for operation nodes.
        :return: A parsed node corresponding to the token.
        """
        if index is None:
            index = self._state.get_current()
        token = self._state.retrieve_token(index)
        if token.is_token_type(TokenType.PRINT):
            return self._parse_statement(self._parse_print_token())
        if token.is_token_type(TokenType.IDENTIFIER):
            if self._is_reassignment_statement(index):
                return self._parse_statement(self._parse_reassignment())
            return self._parse_identifier_token(index)
        if token.is_token_type(TokenType.VAR):
            return self._parse_statement(self._parse_var_token())
        if token.is_token_type(TokenType.IF):
            return self._parse_if_statement()
        if token.is_token_type(TokenType.BREAK):
            return self._parse_statement(self._parse_break())
        if token.is_token_type(TokenType.CONTINUE):
            return self._parse_statement(self._parse_continue())
        if token.is_token_type(TokenType.LOOP):
            return self._parse_loop()
        if token.is_token_type(TokenType.FUNCTION):
            return self._parse_function_declaration()
        if token.is_token_type(TokenType.RETURN):
            return self._parse_statement(self._parse_return())
        if token.is_token_type(TokenType.FUNCTION_CALL):
            return self._parse_statement(self.parse_function_call())
        if token.get_token_type() in TokenType.literal_types():
            return self._parse_literal(token)
        if token.get_token_type() in TokenType.operation_types():
            return self._operation_parser.parse(token, context)

    def _parse_statement(self, node):
        """
        Wraps the parsing of the node and ensures the statement ends with a semicolon.

        :param node: The node representing the parsed expression or statement.
        :return: The node, after verifying that the statement is properly terminated.
        :raises SyntaxException: If the statement does not end with a semicolon.
        """
        self._validate_token({TokenType.SEMI_COLON}, "Expected ';' to terminate the statement.")
        return node

    def _parse_print_token(self):
        """
        Parses a print statement. The expected structure is:
        🗣️ <expression> ;

        :return: PrintNode representing the print statement.
        """
        line_number = self._validate_token({TokenType.PRINT}, "Expected '🗣️' for print statement.")
        node_to_print = self._expression_parser.parse()
        return PrintNode(node_to_print, line_number)

    def _validate_token(self, valid_token_types, error_message):
        """
        Validates that the current token matches one of the expected types. Raises a SyntaxException if not.

        :param valid_token_types: A set of token types that are valid while parsing this token.
        :param error_message: The error message to raise if validation fails.
        """
        current_token = self._state.current_token()
        token_line_number = current_token.get_line()
        if current_token.get_token_type() not in valid_token_types:
            raise SyntaxException(token_line_number, f'{error_message} was {current_token}')
        self._state.advance_current()
        return token_line_number

    def _is_reassignment_statement(self, index):
        """
        Determines if an identifier is part of a statement that represents
        a variable reassignment.

        :param index: The index of the identifier token.
        :return: if the statement is for variable reassignment.
        """
        previous_token, next_token = self._state.retrieve_token(index - 1), self._state.retrieve_token(index + 1)
        return next_token.is_token_type(TokenType.EQUAL) and not previous_token.is_token_type(TokenType.VAR)

    def _parse_identifier_token(self, index):
        """
        Parses an identifier token, which represents an individual variable or represents
        a variable reassignment.

        :param index: The index of the identifier token.
        :return: VariableNode representing the variable or ReassignmentNode with variable and new value.
        """
        identifier_token = self._state.retrieve_token(index)
        return VariableNode(identifier_token.get_lexeme(), identifier_token.get_line())

    def _parse_reassignment(self):
        """
        Parses a reassignment statement in the source code.

        :return: ReassignmentNode representing the reassignment of a variable.
        """
        variable_node, value_node, line_number = self._parse_assignment()
        return ReassignmentNode(variable_node, value_node, line_number)

    def _parse_assignment(self):
        """
        Parses an assignment statement in the source code.

        :return: tuple: A tuple containing the following:
            - VariableNode: A node representing the variable being assigned or reassigned.
            - AbstractSyntaxTreeNode: A node representing the value assigned to the variable.
            - int: The line number where the assignment occurs.
        :raises: SyntaxException if the assignment statement is invalid, such as missing an identifier, assignment operator, or semicolon.
        """
        variable_node = self._parse_identifier_token(self._state.get_current())
        line_number = self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for assignment.")
        self._validate_token({TokenType.EQUAL}, "Expected '✍️' for assignment.")
        value_node = self._expression_parser.parse()
        return variable_node, value_node, line_number

    def _parse_var_token(self):
        """
        Parses a variable declaration or assignment. The expected structure is:
        🥸 <identifier> ✍️ <expression> ;

        :return: AssignmentNode representing the variable assignment.
        """
        self._validate_token({TokenType.VAR}, "Expected '🥸' to indicate variable.")
        variable_node, value_node, line_number = self._parse_assignment()
        return AssignmentNode(variable_node, value_node, line_number)

    def _parse_if_statement(self):
        """
        Parses an if statement in the source code.

        :return: An IfNode representing the parsed if statement.
        """
        line_number = self._validate_token({TokenType.IF}, "Expected '🤔' for if statement.")
        condition_node, block_node = self._parse_conditional()
        next_conditional = self._parse_next_if_conditional()
        return IfNode(condition_node, block_node, next_conditional, line_number)

    def _parse_conditional(self):
        """
        Parse the condition and block of an if statement.

        :return: Tuple containing the condition node and block node.
        """
        condition_node = self._expression_parser.parse()
        self._validate_token({TokenType.LEFT_BRACE}, "Expected '{' to begin if statement block.")
        if_block_node = self._parse_block()
        self._validate_token({TokenType.RIGHT_BRACE}, "Expected '}' to begin if statement block.")
        return condition_node, if_block_node

    def _parse_block(self):
        """
        Parses a block of code enclosed in curly braces `{}`. If no closing brace
        is found, it raises a SyntaxException.

        :return: A BlockNode representing the parsed block of code.
        """
        line_number = self._state.current_line_number()
        nodes = []
        while not self._state.current_token().is_token_type(TokenType.RIGHT_BRACE):
            if self._state.is_eof_token():
                raise SyntaxException(self._state.current_token().get_line(), "Missing closing right brace.")
            node = self.handle_token()
            nodes.append(node)
        return BlockNode(nodes, line_number)

    def _parse_next_if_conditional(self):
        """
        Parses an optional elseif block chain in an if statement.

        :return: A BlockNode representing the elseif node or None if not present.
        """
        current_token = self._state.current_token()
        if current_token.is_token_type(TokenType.ELSE):
            return self._parse_else()
        if current_token.get_token_type() not in TokenType.if_statement_tokens():
            return
        if current_token.is_token_type(TokenType.ELSEIF):
            line_number = self._validate_token({TokenType.ELSEIF}, "Expected '🙈' for elseif statement.")
            condition_node, block_node = self._parse_conditional()
            next_conditional = self._parse_next_if_conditional()
            return ElseIfNode(condition_node, block_node, next_conditional, line_number)

    def _parse_else(self):
        """
        Parses an optional else block in an if statement.

        :return: A BlockNode representing the else block or None if no else block is present.
        """
        if self._state.current_token().is_token_type(TokenType.ELSE):
            line_number = self._validate_token({TokenType.ELSE}, "Expected '💅' for else.")
            self._validate_token({TokenType.LEFT_BRACE}, "Expected '{' to begin else block.")
            else_block_node = self._parse_block()
            self._validate_token({TokenType.RIGHT_BRACE}, "Expected '}' to begin else block.")
            return ElseNode(else_block_node, line_number)

    def _parse_break(self):
        """
        Parses a break statement in the source code which is used to exit a loop prematurely.

        :return: A BreakNode representing the break.
        :raise: SyntaxException if the '💥' token or the terminating semicolon is missing.
        """
        line_number = self._validate_token({TokenType.BREAK}, "Expected '💥' for break.")
        return BreakNode(line_number)

    def _parse_continue(self):
        """
        Parses a continue statement in the source code which is used to skip the rest of the current loop.

        :return: A ContinueNode representing the continue.
        :raise: SyntaxException if the '🤓' token or the terminating semicolon is missing.
        """
        line_number = self._validate_token({TokenType.CONTINUE}, "Expected '🤓' for continue.")
        return ContinueNode(line_number)

    def _parse_loop(self):
        """
        Parses a loop in the source code.

        :return: An LoopNode representing the parsed loop.
        """
        line_number = self._validate_token({TokenType.LOOP}, "Expected '🔁' for loop.")
        condition_node = self._expression_parser.parse()
        self._validate_token({TokenType.LEFT_BRACE}, "Expected '{' to begin if statement block.")
        loop_block_node = self._parse_block()
        self._validate_token({TokenType.RIGHT_BRACE}, "Expected '}' to begin if statement block.")
        return LoopNode(condition_node, loop_block_node, line_number)

    def _parse_function_declaration(self):
        """
        Parses a function declaration corresponding to '🛠️' in the source code.

        :return: An FunctionNode representing the parsed function.
        :raises SyntaxException: If the function declaration is malformed (e.g. missing tokens).
        """
        line_number = self._validate_token({TokenType.FUNCTION}, "Expected '🛠️' for function.")
        function_name = self._parse_function_name()
        self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for function declaration.")
        function_arguments = self._parse_function_argument_names()
        self._validate_token({TokenType.LEFT_BRACE}, "Expected '{' to begin if statement block.")
        function_block_node = self._parse_block()
        self._validate_token({TokenType.RIGHT_BRACE}, "Expected '}' to begin if statement block.")
        return FunctionNode(function_name, function_arguments, function_block_node, line_number)

    def _parse_function_name(self):
        """
        Parses an identifier token, which represents a function name.

        :return: FunctionNameNode representing the function name.
        :raises SyntaxException: If the function name is not a valid identifier.
        """
        identifier_token = self._state.current_token()
        return identifier_token.get_lexeme()

    def _parse_function_argument_names(self):
        """
        Parses the argument names for a function.

        :return: A list of argument names (as strings) for the function.
        :raises SyntaxException: If parentheses or arguments are not correctly formatted.
        """
        self._validate_token({TokenType.LEFT_PAREN}, "Expected left parenthesis for function declaration.")
        arguments = []
        while self._state.current_token().is_token_type(TokenType.VAR):
            argument = self._parse_function_argument_name()
            arguments.append(argument)
        self._validate_token({TokenType.RIGHT_PAREN}, "Expected right parenthesis for function declaration.")
        return arguments

    def _parse_function_argument_name(self):
        """
        Parses an individual function argument.

        :return: A string representing the argument name.
        :raises SyntaxException: If the argument declaration is malformed.
        """
        self._validate_token({TokenType.VAR}, "Expected '🥸' for function argument declaration.")
        identifier_token = self._state.current_token()
        self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for function argument declaration.")
        if self._state.current_token().is_token_type(TokenType.COMMA):
            self._validate_token({TokenType.COMMA}, "Expected a comma for function argument declaration.")
        return identifier_token.get_lexeme()

    def _parse_return(self):
        """
        Parses a return statement corresponding to a '🫡' token from a function.

        :return: A ReturnNode representing the return statement and the expression to return.
        :raises SyntaxException: If the return statement is missing or malformed.
        """
        line_number = self._validate_token({TokenType.RETURN}, "Expected '🫡' for a function return.")
        node_to_return = self._expression_parser.parse()
        return ReturnNode(node_to_return, line_number)

    def parse_function_call(self):
        """
        Parses a function call corresponding to '👀' token from the source code.

        :return: A FunctionCallNode representing the function call.
        :raises SyntaxException: If the function call is malformed.
        """
        line_number = self._validate_token({TokenType.FUNCTION_CALL}, "Expected '👀' for a function call.")
        identifier_token = self._state.current_token()
        self._validate_token({TokenType.IDENTIFIER}, "Expected an identifier for function call.")
        arguments = self._parse_function_call_arguments()
        return FunctionCallNode(identifier_token.get_lexeme(), arguments, line_number)

    def _parse_function_call_arguments(self):
        """
        Parses the arguments passed to a function call.

        :return: A list of expression nodes representing the arguments to the function call.
        :raises SyntaxException: If the argument list is malformed or parentheses are unbalanced.
        """
        self._validate_token({TokenType.LEFT_PAREN}, "Expected left parenthesis for function declaration.")
        arguments = []
        while not self._state.current_token().is_token_type(TokenType.RIGHT_PAREN):
            argument_node = self._expression_parser.parse({TokenType.COMMA, TokenType.RIGHT_PAREN})
            arguments.append(argument_node)
            if self._state.current_token().is_token_type(TokenType.COMMA):
                self._validate_token({TokenType.COMMA}, "Expected a comma for function call argument.")
        self._validate_token({TokenType.RIGHT_PAREN}, "Expected right parenthesis for function call.")
        return arguments

    def _parse_literal(self, token):
        """
        Parses a literal token (e.g., string, number, boolean).

        :param token: The literal token to parse.
        :return: Node representing the literal value.
        """
        line_number = self._state.current_line_number()
        if token.is_token_type(TokenType.STRING):
            return StringLiteralNode(token.get_literal(), line_number)
        if token.is_token_type(TokenType.NUMBER):
            return NumberLiteralNode(token.get_literal(), line_number)
        if token.is_token_type(TokenType.TRUE):
            return BooleanLiteralNode(True, line_number)
        if token.is_token_type(TokenType.FALSE):
            return BooleanLiteralNode(False, line_number)

    def get_scope(self):
        return self._block_scope_context

    def set_scope(self, scope):
        self._block_scope_context = scope

    def get_state(self):
        return self._state
