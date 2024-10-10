from lexer.Scanner import Scanner

with open('helloWorld.emo') as f:
    s = f.read()
    scanner = Scanner(s)
    scanner.scan_tokens()
    print(scanner.get_tokens())
