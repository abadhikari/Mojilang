from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_sum_function_with_addition(capsys):
    source_code = """
    🛠 sum(🥸 num1, 🥸 num2) {
      🫡 num1 ➕ num2;
    }

    🗣️(👀sum(1, 2) ➕ 2);
    """
    expected_output = "5.0\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_multiple_sum_function_calls(capsys):
    source_code = """
    🛠 sum(🥸 num1, 🥸 num2) {
      🫡 num1 ➕ num2;
    }

    🗣️(👀sum(2, 3) ➕ 3);
    🗣️(6 ➕ 👀sum(1, 2));
    """
    expected_output = "8.0\n9.0\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
