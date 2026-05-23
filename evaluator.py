from ast_nodes import Number, BinOp, Variable, LetStatement, PrintStatement, Bool, UnaryOp, IfExpression, AssignStatement, Block

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
        
        elif node.operation == "EQUAL":
            return left == right 
        
        elif node.operation == "NOTEQUAL":
            return left != right 
        
        elif node.operation == "LT":
            return left < right
        
        elif node.operation == "GT":
            return left > right
        
        elif node.operation == "LTE":
            return left <= right
        
        elif node.operation == "GTE":
            return left >= right
        
        elif node.operation == "AND":
            return left and right 
        
        elif node.operation == "OR":
            return left or right

        

    # Variable + let + print parts
    if isinstance(node, Variable):
        return env.lookup(node.name)
    
    if isinstance(node, LetStatement):
        value = evaluate(node.value, env)
        env.define(node.name, value)
        return None
    
    if isinstance(node, PrintStatement):
        value = evaluate(node.expr, env)
        # lowering the first characters of "T"rue and "F"alse
        if isinstance(value, bool):
            print(str(value).lower())
        else:
            print(value)
        return None
    
    # bool part
    if isinstance(node, Bool):
        return node.value
    
    # unary evaluation
    if isinstance(node, UnaryOp):
        value = evaluate(node.expression, env)

        if node.operation == "NOT":
            return not value
        
    # if block evaluation
    if isinstance(node, IfExpression):
        condition = evaluate(node.condition, env)

        if condition:
            return evaluate(node.then_branch, env)
        else:
            return evaluate(node.else_branch, env)
        
    # assignment evaluation
    if isinstance(node, AssignStatement):
        value = evaluate(node.value, env)
        env.assign(node.name, value)
        return None
    
    # evaluating blocks
    if isinstance(node, Block):
        result = None

        for statement in node.statements:
            result = evaluate(statement, env)

        return result