class Environment:

    def __init__(self, parent = None):
        self.values = {}
        self.parent = parent

    def define(self, name, value):
        self.values[name] = value

    def lookup(self, name):
        if name in self.values:
            return self.values[name]
        
        if self.parent is not None:
            return self.parent.lookup(name)
        
        raise Exception(f"Undefined Variable! -> {name}")

    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
            return
        if self.parent is not None:
            self.parent.assign(name, value)
            return 
        raise Exception(f"Undefined variable! ->{name}")