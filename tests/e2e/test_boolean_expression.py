from emolang import Parser, Interpreter, Lexer


def test_logical_and_comparison_operations(capsys):
    source_code = """
    🥸 isTrueAnd ✍️ 😤 and 😔;
    🥸 isTrueOr ✍️ 😤 or 😔;
    🥸 isEquivalent ✍️ 4 🙅🤝 (8 ➗ 2) ✖️3;
    🥸 isGreater ✍️ 4 ☝️ (8 ➗ 2) ✖️3;
    🥸 isLess ✍️ 4 👇 (8 ➗ 2) ✖️3;
    🥸 notIsLess ✍️ 🙅isLess;
    🗣️(isTrueAnd);
    🗣️(isTrueOr);
    🗣️(isEquivalent);
    🗣️(isGreater);
    🗣️(isLess);
    🗣️(notIsLess);
    """

    lexer = Lexer(source_code)
    lexer.scan_tokens()

    parser = Parser(lexer.get_tokens())
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.execute()

    captured = capsys.readouterr()

    expected_output = "😔\n😤\n😤\n😔\n😤\n😔\n"

    assert captured.out == expected_output
