# A lexical token is a sequence of characters that can be treated as a unit in the grammar of the
# programming languages

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)


class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)


class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR(?)", value)  # value for variable name
        # VAR for a token of type variable, (?) for unknown variable's data type
