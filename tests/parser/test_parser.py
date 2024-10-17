import pytest
from emolang.lexer import Lexer, SyntaxException
from emolang.parser import Parser
from emolang.parser.nodes import (
    AdditionNode,
    AssignmentNode,
    AndNode,
    BlockNode,
    PrintNode,
    VariableNode,
    MultiplicationNode
)


@pytest.fixture
def lexer():
    def create_tokens(source_code):
        lex = Lexer(source_code)
        lex.scan_tokens()
        return lex.get_tokens()
    return create_tokens


def test_simple_assignment(lexer):
    source_code = "🥸 x ✍️ 5;"
    tokens = lexer(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    assert isinstance(ast, BlockNode)
    assert len(ast.get_nodes()) == 1
    assignment_node = ast.get_nodes()[0]
    assert isinstance(assignment_node, AssignmentNode)
    assert assignment_node._variable_node.get_name() == "x"


def test_boolean_operations(lexer):
    source_code = "🥸 trueAndFalse ✍️ 😤 and 😔;"
    tokens = lexer(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    assert isinstance(ast, BlockNode)
    assert len(ast.get_nodes()) == 1
    assignment_node = ast.get_nodes()[0]
    assert isinstance(assignment_node, AssignmentNode)
    assert assignment_node.get_variable_node().get_name() == "trueAndFalse"
    assert isinstance(assignment_node.get_value_node(), AndNode)
    assert assignment_node.get_value_node().evaluate({}) is False


def test_arithmetic_expression(lexer):
    source_code = "🥸 result ✍️ (3 ➕ 2) ✖️ 4;"
    tokens = lexer(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    assert isinstance(ast, BlockNode)
    assert len(ast.get_nodes()) == 1
    assignment_node = ast.get_nodes()[0]
    assert isinstance(assignment_node, AssignmentNode)
    assert assignment_node.get_variable_node().get_name() == "result"
    assert isinstance(assignment_node.get_value_node(), MultiplicationNode)
    assert isinstance(assignment_node.get_value_node().get_left_operand(), AdditionNode)
    assert assignment_node.get_value_node().evaluate({}) == 20


def test_print_statement(lexer):
    source_code = "🗣️(isTrueAnd);"
    tokens = lexer(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    assert isinstance(ast, BlockNode)
    assert len(ast.get_nodes()) == 1
    print_node = ast.get_nodes()[0]
    assert isinstance(print_node, PrintNode)
    assert isinstance(print_node.get_node_to_print(), VariableNode)
    assert print_node.get_node_to_print().get_name() == "isTrueAnd"


def test_invalid_syntax(lexer):
    source_code = "🥸 variable ✍️ ;"
    tokens = lexer(source_code)
    parser = Parser(tokens)

    with pytest.raises(SyntaxException):
        parser.parse()
