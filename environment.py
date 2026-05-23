class Environment:

    def __init__(self):
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def lookup(self, name):
        if name in self.values:
            return self.values[name]
        raise Exception(f"Undefined Variable! -> {name}")
