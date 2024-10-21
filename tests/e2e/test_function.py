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


def test_multiple_functions(capsys):
    source_code = """
    🛠️sum(🥸 num1, 🥸 num2) {
    🫡 num1 + num2;
    }
    
    🛠️isEqual(🥸 num1, 🥸 num2) {
    🫡 num1 == num2;
    }

    🥸 summed_numbers = 👀sum(3, 2);
    🗣️ summed_numbers;
    🥸 are_equal = 👀isEqual(summed_numbers, 5);
    🗣️ are_equal;
    """
    expected_output = "5.0\n😤\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
