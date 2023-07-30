from lexer import Lexer

while True:
    text = input("[cil] > ")
    if text == "exit":
        break
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    print(tokens)
