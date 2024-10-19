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
    expected_output = "10.0\n9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\nBlast off!\n"
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
    expected_output = "5.0\n4.0\n3.0\nLoop exited.\n"
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
    expected_output = "5.0\n3.0\n1.0\nLoop completed.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
