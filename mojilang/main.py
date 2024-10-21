from mojilang.lexer import Lexer
from mojilang.parser import Parser
from mojilang.interpreter import Interpreter
from mojilang.lexer import SyntaxException

with open('mojilang/mojilang_files/function.moji') as f:
    s = f.read()
    moji_lexer = Lexer(s)
    exceptions = moji_lexer.scan_tokens()

    if exceptions:
        raise SyntaxException(12, f'Found the following syntax errors: {exceptions}')

    tokens = moji_lexer.get_tokens()
    print(tokens)

    moji_parser = Parser(tokens)
    abstract_syntax_tree = moji_parser.parse()

    moji_interpreter = Interpreter(abstract_syntax_tree)
    moji_interpreter.execute()
