from ast_nodes import Number, BinOp, Variable, LetStatement, PrintStatement, Bool, UnaryOp, IfExpression

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

        expr = self.parse_or()

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
            node = self.parse_or()
            self.eat("RIGHTPARENTHESIS")
            return node
        
        # not gate
        elif token.type == "NOT":
            self.eat("NOT")

            expr = self.parse_factor()

            return UnaryOp("NOT", expr)
        
        # if block detection
        elif token.type == "IF":
            return self.parse_if()
        
        raise Exception(f"Unexpected tpken! -> {token}")
    
    def parse_let(self):
        self.eat("LET")

        name_token = self.eat("IDENTIFIER")
        self.eat("EQUAL")

        value = self.parse_or()

        self.eat("SEMICOLON")

        return LetStatement(name_token.value, value)
    
    def parse_statement(self):
        token = self.current()

        if token.type == "LET":
            return self.parse_let()
        
        if token.type == "PRINT":
            return self.parse_print()
        
        expr = self.parse_or()
        self.eat("SEMICOLON")
        return expr
    
    def parse_program(self):
        statements = []

        while self.current() is not None:
            statements.append(self.parse_statement())
        return statements

    def parse_comparison(self):
        node = self.parse_expression()

        if self.current() and self.current().type in ("EQUAL", "NOTEQUAL", "LT", "GT", "LTE", "GTE"):
            operation = self.current()
            self.eat(operation.type)

            right = self.parse_expression()
            node = BinOp(node, operation.type, right)

        return node

    def parse_and(self):
        node = self.parse_comparison()

        while self.current() and self.current().type == "AND":
            operation = self.current()
            self.eat("AND")

            right = self.parse_comparison()

            node = BinOp(node, operation.type, right)
        return node
    
    def parse_or(self):
        node = self.parse_and()

        while self.current() and self.current().type == "OR":
            operation = self.current()
            self.eat("OR")

            right = self.parse_and()

            node = BinOp(node, operation.type, right)
        return node
    
    # for every high level addition expression - comparison - and - or we need to update the first call in other blocks

    def parse_if(self):
        self.eat("IF")
        condition = self.parse_or()

        self.eat("THEN")
        then_branch = self.parse_or()

        self.eat("ELSE")
        else_branch = self.parse_or()

        self.eat("END")
        return IfExpression(condition, then_branch, else_branch)