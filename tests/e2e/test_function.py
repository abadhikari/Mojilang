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


def test_function_scope_shadowing(capsys):
    source_code = """
    🛠 add_two_to_x() {
        🥸 x ✍️ 3;
        🫡 x ➕ 2;
    }

    🥸 x ✍️ 2;
    🗣️(x);
    🗣️(👀add_two_to_x());
    🗣️(x);
    """
    expected_output = "2.0\n5.0\n2.0\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_function_incorrect_variable_reassignment(capsys):
    source_code = """
    🛠 add_two_to_x() {
        x ✍️ 3;
        🫡 x ➕ 2;
    }

    🥸 x ✍️ 2;
    🗣️(x);
    🗣️(👀add_two_to_x());
    🗣️(x);
    """
    try:
        run_interpreter_and_retrieve_output(source_code, capsys)
    except RuntimeError as e:
        assert "line 3, mojilang Runtime Error: Variable has not been declared yet." in str(e)


def test_function_closure(capsys):
    source_code = """
    🛠 outer_function() {
        🥸 x = 10;
        🥸 y = 1;
        🛠 inner_function() {
            🥸 x = 20;
            🗣️ x;
            🗣️ y;
        }
        👀 inner_function();
        🗣️ x;
    }
    🥸 x = 5;
    🗣️ x;
    👀 outer_function();
    """
    expected_output = "5.0\n20.0\n1.0\n10.0\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
