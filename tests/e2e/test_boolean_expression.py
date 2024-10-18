from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_logical_and_operation_is_false(capsys):
    source_code = """
    🥸 isTrueAnd ✍️ 😤 and 😔;
    🗣️(isTrueAnd);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_logical_and_both_true(capsys):
    source_code = """
    🥸 bothTrueAnd ✍️ 😤 and 😤;
    🗣️(bothTrueAnd);
    """
    expected_output = "😤\n"
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


def test_logical_or_both_false(capsys):
    source_code = """
    🥸 bothFalseOr ✍️ 😔 or 😔;
    🗣️(bothFalseOr);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_not_operation_on_true(capsys):
    source_code = """
    🥸 notTrue ✍️ 🙅😤;
    🗣️(notTrue);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_not_operation_on_false(capsys):
    source_code = """
    🥸 notFalse ✍️ 🙅😔;
    🗣️(notFalse);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_multiple_not_operations(capsys):
    source_code = """
    🥸 multipleNot ✍️ 🙅🙅🙅😤;
    🗣️(multipleNot);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_equality_of_same_numbers(capsys):
    source_code = """
    🥸 isEqualNumbers ✍️ 5 🤝 5;
    🗣️(isEqualNumbers);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_equality_comparison_is_false(capsys):
    source_code = """
    🥸 isEqual ✍️ 5 🤝 4;
    🗣️(isEqual);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_inequality_comparison_is_true(capsys):
    source_code = """
    🥸 isNotEqual ✍️ 5 🙅🤝 4;
    🗣️(isNotEqual);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_inequality_with_expressions_is_true(capsys):
    source_code = """
    🥸 isNotEqualExpr ✍️ 4 🙅🤝 (8 ➗ 2) ✖️3;
    🗣️(isNotEqualExpr);
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


def test_greater_than_or_equal_comparison_is_true(capsys):
    source_code = """
    🥸 isGreaterOrEqual ✍️ 5 ☝🤝 5;
    🗣️(isGreaterOrEqual);
    """
    expected_output = "😤\n"
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


def test_less_than_or_equal_comparison_is_false(capsys):
    source_code = """
    🥸 isLessOrEqual ✍️ 4 👇🤝 3;
    🗣️(isLessOrEqual);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_combined_and_or_operations(capsys):
    source_code = """
    🥸 combinedOperation ✍️ (😤 and 😔) or 😤;
    🗣️(combinedOperation);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_combined_comparison_and_logical_operations(capsys):
    source_code = """
    🥸 combinedComparison ✍️ (4 👇 5) and (6 ☝️ 3);
    🗣️(combinedComparison);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_nested_parentheses_operations(capsys):
    source_code = """
    🥸 nestedOperation ✍️ (4 👇 (8 ➗ 2)) and ((3 ➕ 2) ☝️ 4);
    🗣️(nestedOperation);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_combined_arithmetic_and_comparison(capsys):
    source_code = """
    🥸 combinedArithComparison ✍️ (3 ➕ 2) ☝️ (5 ➖ 1);
    🗣️(combinedArithComparison);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_multiple_comparisons_with_logical_operations(capsys):
    source_code = """
    🥸 multiCompLogical ✍️ (4 ☝️ 2) and (5 👇 6) or (7 🙅🤝 7);
    🗣️(multiCompLogical);
    """
    expected_output = "😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_complex_nested_logical_operations(capsys):
    source_code = """
    🥸 complexLogic ✍️ 🙅(😤 or (😔 and (😤 or 😔)));
    🗣️(complexLogic);
    """
    expected_output = "😔\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output