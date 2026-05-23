from ast_nodes import Number, BinOp

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0


    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    # consuming the current token if it is matching the expected type
    def eat(self, token_type):
        token = self.current()

        if token.type == token_type:
            self.pos += 1
            return token

        raise Exception(f"Expected {token_type}")
    
    def parse_factor(self):
        token = self.current()

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return Number(token.value)
    
        elif token.type == "LEFTPARENTHESIS":

            self.eat("LEFTPARENTHESIS")
            node = self.parse_expression()
            self.eat("RIGHTPARENTHESIS")
            return node
        
    def parse_term(self):
        node = self.parse_factor()

        while self.current() and self.current().type in ("STAR", "SLASH"):
            op = self.current()
            self.eat(op.type)

            right = self.parse_factor()

            node = BinOp(node, op.type, right)

        return node
    
    def parse_expression(self):
        node = self.parse_term()

        while self.current() and self.current().type in ("PLUS", "MINUS"):
            op = self.current()
            self.eat(op.type)

            right = self.parse_term()

            node = BinOp(node, op.type, right)

        return node