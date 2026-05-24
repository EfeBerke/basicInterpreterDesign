# Efe Berke Vatansever, 2025402006
class Environment:

    def __init__(self, parent = None):
        self.values = {}
        self.parent = parent

    # defining new variable
    def define(self, name, value):
        self.values[name] = value

    # finding the variable value
    def lookup(self, name):
        # checking current scope
        if name in self.values:
            return self.values[name]
        
        # checking parent scope
        if self.parent is not None:
            return self.parent.lookup(name)
        
        # if variable not found raise error
        raise Exception(f"Undefined Variable! -> {name}")

    # updating the existing variable 
    def assign(self, name, value):
        # local update 
        if name in self.values:
            self.values[name] = value
            return
        # searching parent for assignment
        if self.parent is not None:
            self.parent.assign(name, value)
            return 
        # if not found for assignment raise error
        raise Exception(f"Undefined variable! ->{name}")