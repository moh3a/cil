# Take the generated parse tree as input and interpret it (compute arithmetic expression, for now)
# Should be done with a postorder traversal of the binary tree

from tokens import Integer, Float


class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def read_VAR(self, id):
        variable = self.data.read(id)
        variable_type = variable.type

        return getattr(self, f"read_{variable_type}")(variable.value)

    def compute_bin(self, left, op, right):
        left_type = "VAR" if str(left.type).startswith(
            "VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith(
            "VAR") else str(right.type)

        if op.value == "=":
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

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

    def compute_unary(self, operator, operand):
        operand_type = "VAR" if str(operand.type).startswith(
            "VAR") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value)

        if operator.value == "+":
            return +operand
        elif operator.value == "-":
            return -operand

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        # interpret a unary operation
        if isinstance(tree, list) and len(tree) == 2:
            return self.compute_unary(tree[0], tree[1])

        # no operation
        # if input is not a tree return the number, example: 1 -> Integer("INT", 1)
        elif not isinstance(tree, list):
            return tree

        else:
            #    A
            #   / \
            #  B   C
            #
            # [B, A, C]

            left_node = tree[0]  # left subtree B
            if isinstance(left_node, list):
                # recursively interpret every subtree of the node
                left_node = self.interpret(left_node)

            right_node = tree[2]  # right subtree C
            if isinstance(right_node, list):
                right_node = self.interpret(right_node)

            operator = tree[1]  # root node A

            return self.compute_bin(left_node, operator, right_node)
