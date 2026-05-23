from ast_nodes import Number, BinOp, Variable, LetStatement, PrintStatement, Bool

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
    
    def parse_print(self):
        self.eat("PRINT")
        self.eat("LEFTPARENTHESIS")

        expr = self.parse_expression()

        self.eat("RIGHTPARENTHESIS")
        self.eat("SEMICOLON")

        return PrintStatement(expr)

    def parse_factor(self):
        token = self.current()

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return Number(token.value)
        
        elif token.type == "TRUE":
            self.eat("TRUE")
            return Bool(True)
        
        elif token.type == "FALSE":
            self.eat("FALSE")
            return Bool(False)
        
        elif token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            return Variable(token.value)
        
        elif token.type == "LEFTPARENTHESIS":
            self.eat("LEFTPARENTHESIS")
            node = self.parse_expression()
            self.eat("RIGHTPARENTHESIS")
            return node

        raise Exception(f"Unexpected tpken! -> {token}")
    
    def parse_let(self):
        self.eat("LET")

        name_token = self.eat("IDENTIFIER")
        self.eat("EQUAL")

        value = self.parse_expression()

        self.eat("SEMICOLON")

        return LetStatement(name_token.value, value)
    
    def parse_statement(self):
        token = self.current()

        if token.type == "LET":
            return self.parse_let()
        
        if token.type == "PRINT":
            return self.parse_print()
        
        expr = self.parse_expression()
        self.eat("SEMICOLON")
        return expr
    
    def parse_program(self):
        statements = []

        while self.current() is not None:
            statements.append(self.parse_statement())
        return statements


        
