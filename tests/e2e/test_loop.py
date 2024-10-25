from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_while_loop_basic_countdown(capsys):
    """
    Test a basic countdown using a while loop, starting from 10 and ending at 1.
    """
    source_code = """
    🥸 i ✍️ 10;
    🔁(i ☝️ 0) {
        🗣️(i);
        i ✍️ i ➖ 1;
    }
    🗣️("Blast off!");
    """
    expected_output = "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nBlast off!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_while_loop_zero_iterations(capsys):
    """
    Test a while loop where the initial condition is false, so the loop body does not execute.
    """
    source_code = """
    🥸 i ✍️ 0;
    🔁(i ☝️ 0) {
        🗣️("This should not print.");
    }
    🗣️("Loop ended.");
    """
    expected_output = "Loop ended.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_break_in_loop(capsys):
    source_code = """
    🥸 i ✍️ 5;
    🔁(i ☝️ 0) {
        🗣️(i);
        🤔(i 🤝 3) {
            💥;
        }
        i ✍️ i ➖ 1;
    }
    🗣️("Loop exited.");
    """
    expected_output = "5\n4\n3\nLoop exited.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_continue_for_even_numbers_in_loop(capsys):
    source_code = """
    🥸 i ✍️ 6;
    🔁(i ☝️ 0) {
        i ✍️ i ➖ 1;
        🤔(i 🍕 2 🤝 0) {
            🤓;
        }
        🗣️(i);
    }
    🗣️("Loop completed.");
    """
    expected_output = "5\n3\n1\nLoop completed.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_assign_variable_inside_loop(capsys):
    source_code = """
    🥸 i ✍️ 3;
    🔁(i ☝️ 0) {
        🥸 new_var ✍️ i ➕ 10;
        🗣️(new_var);
        i ✍️ i ➖ 1;
    }
    🗣️("Loop completed.");
    """
    expected_output = "13\n12\n11\nLoop completed.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
