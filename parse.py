# to learn more: http://www.cs.man.ac.uk/~pjj/farrell/comp4.html
# take the lexical analysis result, and build a parse tree (b-tree)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    # factor : 	    number | ( expression ) | + factor | − factor
    def factor(self):
        # number
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        # expression
        elif self.token.value == "(":
            self.move()
            expression = self.expression()
            return expression
        # variable assertion
        elif self.token.type.startswith("VAR"):
            return self.token
        # unary operation
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            operand = self.factor()
            return [operator, operand]

    # term :        factor | factor * factor | factor / factor
    # example: 1 * 2 -> [1, *, 2]
    def term(self):
        left_node = self.factor()
        self.move()
        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operation, right_node]

        return left_node

    # expression :	term | term + term | term − term
    def expression(self):
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token

    def statement(self):
        if self.token.type == "DECL":
            # variable statement
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.expression()
                return [left_node, operation, right_node]

        elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OP":
            # artithmetic expression
            return self.expression()

    def parse(self):
        return self.statement()

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
