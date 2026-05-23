from ast_nodes import Number, BinOp

def evaluate(node):

    if isinstance(node, Number):
        return node.value

    if isinstance(node, BinOp):

        left = evaluate(node.left)
        right = evaluate(node.right)

        if node.operation == "PLUS":
            return left + right

        elif node.operation == "MINUS":
            return left - right

        elif node.operation == "STAR":
            return left * right

        elif node.operation == "SLASH":
            return int(left / right)