from mojilang.lexer import Lexer
from mojilang.parser import Parser
from mojilang.interpreter import Interpreter

with open('mojilang/mojilang_files/loop.moji') as f:
    s = f.read()
    emo_lexer = Lexer(s)
    emo_lexer.scan_tokens()
    tokens = emo_lexer.get_tokens()
    print(tokens)

    emo_parser = Parser(tokens)
    abstract_syntax_tree = emo_parser.parse()

    emo_interpreter = Interpreter(abstract_syntax_tree)
    emo_interpreter.execute()