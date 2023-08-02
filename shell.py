from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("[cil] > ")
    if text == "exit":
        break

    # Regardless of where the program comes from it must first pass through a Tokenizer, or as it is sometimes called, a Lexer. The tokenizer is responsible for dividing the input stream into individual tokens, identifying the token type, and passing tokens one at a time to the next stage of the compiler.
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    # The next stage of the compiler is called the Parser. This part of the compiler has an understanding of the language's grammar. It is responsible for identifying syntax errors and for translating an error free program into internal data structures that can be interpreted or written out in another language.
    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()

    print(result)
