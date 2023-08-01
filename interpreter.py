# Take the generated parse tree as input and interpret it (compute arithmetic expression, for now)
# Should be done with a postorder traversal of the binary tree

from tokens import Integer, Float

class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def compute_bin(self, left, op, right):
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)

    def interpret(self, tree = None):
        if tree is None:
            tree = self.tree

        #    A
        #   / \
        #  B   C
        #
        # [B, A, C]

        left_node = tree[0] # left subtree B
        if isinstance(left_node, list):
            left_node = self.interpret(left_node) # recursively interpret every subtree of the node
        
        right_node = tree[2] # right subtree C
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1] # root node A

        return self.compute_bin(left_node, operator, right_node)
        
