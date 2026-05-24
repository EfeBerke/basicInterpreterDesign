class Number:
    def __init__(self, value):
        self.value = value

"""
why ast is for ?
3 + (4 * 2)
-----------------
        +
      /   \\
     3     *
          / \\ 
         4   2
"""
class BinOp:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

# variables, let and print classes
class Variable:
    def __init__(self, name):
        self.name = name

class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintStatement:
    def __init__(self, expr):
        self.expr = expr
    
# Boolean values
class Bool:
    def __init__(self, value):
        self.value = value

# Unary operations for logical operations
class UnaryOp:
    def __init__(self, operation, expression):
        self.operation = operation
        self.expression = expression

# If expression class
class IfExpression:
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

# Assigning Statement
class AssignStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Block expression
class Block:
    def __init__(self, statements):
        self.statements = statements

# fun function
class FunExpression:
    def __init__(self, params, body):
        self.params = params
        self.body = body

# call function class
class CallExpression:
    def __init__(self, func, args):
        self.func = func
        self.args = args

