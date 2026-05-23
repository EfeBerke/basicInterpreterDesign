class Number:
    def __init__(self, value):
        self.value = value

"""
why ast is for ?
3 + (4 * 2)
-----------------
        +
      /   \ 
     3     *
          / \ 
         4   2
"""
class BinOp:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right


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
    
