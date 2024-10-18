from .run_interpreter import run_interpreter_and_retrieve_output


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
