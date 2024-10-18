from .run_interpreter import run_interpreter_and_retrieve_output


def test_logical_and_operation_is_false(capsys):
    source_code = """
    🥸 isTrueAnd ✍️ 😤 and 😔;
    🗣️(isTrueAnd);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_logical_or_operation_is_true(capsys):
    source_code = """
    🥸 isTrueOr ✍️ 😤 or 😔;
    🗣️(isTrueOr);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_equality_comparison_is_true(capsys):
    source_code = """
    🥸 isEquivalent ✍️ 4 🙅🤝 (8 ➗ 2) ✖️3;
    🗣️(isEquivalent);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_greater_than_comparison_is_false(capsys):
    source_code = """
    🥸 isGreater ✍️ 4 ☝️ (8 ➗ 2) ✖️3;
    🗣️(isGreater);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_less_than_comparison_is_true(capsys):
    source_code = """
    🥸 isLess ✍️ 4 👇 (8 ➗ 2) ✖️3;
    🗣️(isLess);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_not_operation_is_false(capsys):
    source_code = """
    🥸 isLess ✍️ 4 👇 (8 ➗ 2) ✖️3;
    🥸 notIsLess ✍️ 🙅isLess;
    🗣️(notIsLess);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
