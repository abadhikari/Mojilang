from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_variable_shadowing_in_loop(capsys):
    source_code = """
    🥸 i ✍️ 5;
    🥸 shadow_var ✍️ 100;
    🔁(i ☝️ 0) {
        🥸 shadow_var ✍️ i ➕ 10;
        🗣️(shadow_var);
        i ✍️ i ➖ 1;
    }
    🗣️(shadow_var);
    """
    try:
        run_interpreter_and_retrieve_output(source_code, capsys)
    except RuntimeError as e:
        expected_output = "Variable has already been declared. Cannot redeclare."
        assert expected_output in str(e)


def test_variable_scope_in_if_statement(capsys):
    source_code = """
    🥸 x ✍️ 10;
    🤔(x 🤝 10) {
        🥸 if_var ✍️ x ➕ 20;
        🗣️(if_var);
    }
    🗣️(if_var);
    """
    try:
        run_interpreter_and_retrieve_output(source_code, capsys)
    except RuntimeError as e:
        assert "Syntax error at line 7: Undefined variable 'if_var'" in str(e)


def test_variable_scope_in_nested_if_statement(capsys):
    source_code = """
    🥸 x ✍️ 10;
    🤔(x 🤝 10) {
        🥸 y ✍️ x ➕ 5;
        🤔(y 🤝 15) {
            🥸 z ✍️ y ➕ 10 ➕ x;
            🤔(z 🤝 35) {
                🗣️(z);
            }
        }
    }
    """
    expected_output = "35\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_reassign_global_variable_inside_loop(capsys):
    source_code = """
    🥸 global_var ✍️ 0;
    🥸 i ✍️ 3;
    🔁(i ☝️ 0) {
        global_var ✍️ global_var ➕ i;
        i ✍️ i ➖ 1;
    }
    🗣️(global_var);
    """
    expected_output = "6\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_multiple_variable_scopes(capsys):
    source_code = """
    🥸 i ✍️ 2;
    🔁(i ☝️ 0) {
        🥸 inner_i ✍️ 5;
        🗣️(inner_i);
        🔁(inner_i ☝️ 0) {
            🥸 nested_var ✍️ inner_i ➕ i;
            🗣️(nested_var);
            inner_i ✍️ inner_i ➖ 1;
        }
        i ✍️ i ➖ 1;
    }
    """
    expected_output = "5\n7\n6\n5\n4\n3\n5\n6\n5\n4\n3\n2\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
