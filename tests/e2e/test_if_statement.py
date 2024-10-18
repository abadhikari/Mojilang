from tests.e2e.utils.run_interpreter import run_interpreter_and_retrieve_output


def test_if_statement_true_case(capsys):
    source_code = """
    🥸 age ✍️ 25;
    🤔(age ☝️ 21) {
        🗣️("You can drink 😤!");
    } 💅 {
        🗣️("You can't drink 😔!");
    }
    """
    expected_output = "You can drink 😤!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_if_statement_true_case_with_multiple_statements(capsys):
    source_code = """
    🥸 age ✍️ 25;
    🤔 (age ☝️ 21) {
        🗣️("You can drink 😤!");
        🗣️("We're going out tonight!");
    } 💅 {
        🗣️("You can't drink 😔.");
    }
    """
    expected_output = "You can drink 😤!\nWe're going out tonight!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_if_statement_else_case(capsys):
    source_code = """
    🥸 age ✍️ 20;
    🤔(age ☝️ 21) {
        🗣️("You can drink 😤!");
    } 💅 {
        🗣️("You can't drink 😔!");
    }
    """
    expected_output = "You can't drink 😔!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_if_statement_without_else_case(capsys):
    source_code = """
    🥸 age ✍️ 20;
    🤔(age ☝️ 21) {
        🗣️("You can drink 😤!");
    }
    """
    expected_output = ""
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_if_statement_with_complex_condition(capsys):
    source_code = """
    🥸 temperature ✍️ 75;
    🥸 isSunny ✍️ 😤;
    🤔(temperature ☝️ 70 and isSunny) {
        🗣️("It's a great day for a picnic!");
    } 💅 {
        🗣️("Maybe stay indoors today.");
    }
    """
    expected_output = "It's a great day for a picnic!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_nested_if_statements(capsys):
    source_code = """
    🥸 age ✍️ 67;
    🤔(age ☝️ 18) {
        🗣️("You are an adult.");
        🤔(age ☝️ 65) {
            🗣️("You are eligible for senior discounts.");
        }
    }
    """
    expected_output = "You are an adult.\nYou are eligible for senior discounts.\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output


def test_if_else(capsys):
    source_code = """
    🥸 age ✍️ 22;
    🤔(age 🤝 23) {
        🗣️("You're 23, you can drink 😤!");
    } 🙈(age 🤝 22) {
        🗣️("You're 22, you can drink 😤!");
    } 🙈(age ☝️ 21) {
        🗣️("You're above 21, you can drink 😤!");
    } 💅 {
        🗣️("You can't drink 😔!");
    }
    """
    expected_output = "You're 22, you can drink 😤!\n"
    captured = run_interpreter_and_retrieve_output(source_code, capsys)
    assert captured.out == expected_output
