from mojilang.lexer import SyntaxException
from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_variable_reassignment(capsys):
    source_code = """
    🥸 x ✍️ 10;
    🗣️(x);
    x ✍️ 20;
    🗣️(x);
    """
    expected_output = "10\n20\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_reassignment_with_expression(capsys):
    source_code = """
    🥸 y ✍️ 5;
    🗣️(y);
    y ✍️ y ➕ 10;
    🗣️(y);
    """
    expected_output = "5\n15\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_reassignment_without_initial_declaration(capsys):
    source_code = """
    x ✍️ 20;
    """
    try:
        run_interpreter_and_retrieve_output(source_code, capsys)
        assert False, "Expected RuntimeException for undeclared variable."
    except RuntimeError as e:
        assert str(e) == "Execution error: line 2, mojilang Runtime Error: Variable has not been declared yet."


def test_multiple_reassignments(capsys):
    source_code = """
    🥸 z ✍️ 1;
    🗣️(z);
    z ✍️ 2;
    🗣️(z);
    z ✍️ 3;
    🗣️(z);
    """
    expected_output = "1\n2\n3\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_invalid_reassignment_syntax(capsys):
    source_code = """
    🥸 a ✍️ 10;
    a ✍️ 20 
    """
    try:
        run_interpreter_and_retrieve_output(source_code, capsys)
        assert False, "Expected SyntaxException for missing semicolon."
    except SyntaxException as e:
        assert "Expected ';' to terminate the statement." in str(e)
