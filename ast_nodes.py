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