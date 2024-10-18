from emolang import Parser, Interpreter, Lexer


def run_interpreter_and_retrieve_output(source_code, capsys):
    lexer = Lexer(source_code)
    lexer.scan_tokens()

    parser = Parser(lexer.get_tokens())
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.execute()

    return capsys.readouterr()
