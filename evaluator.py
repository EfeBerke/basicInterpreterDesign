from ast_nodes import Number, BinOp, Variable, LetStatement, PrintStatement

def evaluate(node, env):

    if isinstance(node, Number):
        return node.value

    if isinstance(node, BinOp):

        left = evaluate(node.left, env)
        right = evaluate(node.right, env)

        if node.operation == "PLUS":
            return left + right

        elif node.operation == "MINUS":
            return left - right

        elif node.operation == "STAR":
            return left * right

        elif node.operation == "SLASH":
            return int(left / right)
        

    # Variable + let + print parts
    if isinstance(node, Variable):
        return env.lookup(node.name)
    
    if isinstance(node, LetStatement):
        value = evaluate(node.value, env)
        env.define(node.name, value)
        return None
    if isinstance(node, PrintStatement):
        value = evaluate(node.expr, env)
        print(value)
        return None