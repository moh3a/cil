# A lexical analysis, lexing or tokenization is the process of converting a sequence of characters 
# into a sequence of lexical tokens. A program that performs lexical analysis may be termed a 
# lexer, tokenizer or scanner. A lexer is generally combined with a parser, which together analyze 
# the syntax of programming languages, web pages, and so forth

class Lexer:
    digits = "0123456789"
    operations = "+-/*"
    stop_words = [" "]

    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()
            elif self.char in Lexer.stop_words:
                self.move()
                continue

            self.tokens.append(self.token)
        
        return self.tokens

    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)

    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

# A lexical token is a sequence of characters that can be treated as a unit in the grammar of the 
# programming languages
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return self.value

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)

class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)
