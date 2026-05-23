# converter from characters to tokens
class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"
    

# skeleton of the tokenizer

def tokenize(text):
    tokens = []
    i = 0

    while i < len(text):
        char = text[i]

        if char.isspace():
            i += 1

        # handling the alphabethic characters for let, print and variables      
        elif char.isalpha():
            word = ""

            while i < len(text) and (text[i].isalnum() or text[i] == "_"):
                word += text[i]
                i += 1

            if word == "let":
                tokens.append(Token("LET"))
            elif word == "print":
                tokens.append(Token("PRINT"))
            # handling boolean parts
            elif word == "true":
                tokens.append(Token("TRUE", True))
            elif word == "false":
                tokens.append(Token("FALSE", False))
            else:
                tokens.append(Token("IDENTIFIER", word))
                
        elif text[i:i+2] == "==":
            tokens.append(Token("EQUAL"))
            i += 2

        elif text[i:i+2] == "!=":
            tokens.append(Token("NOTEQUAL"))
            i += 2

        elif text[i:i+2] == "<=":
            tokens.append(Token("LTE"))
            i += 2

        elif text[i:i+2] == ">=":
            tokens.append(Token("GTE"))
            i += 2 

        elif char == "=":
            tokens.append(Token("EQUAL"))
            i += 1

        elif char.isdigit():
            number = ""

            while i < len(text) and text[i].isdigit():
                number += text[i]
                i += 1

            tokens.append(Token("NUMBER", int(number)))

        elif char == "+":
            tokens.append(Token("PLUS"))
            i += 1

        elif char == "-":
            tokens.append(Token("MINUS"))
            i += 1

        elif char == "*":
            tokens.append(Token("STAR"))
            i += 1

        elif char == "/":
            tokens.append(Token("SLASH"))
            i += 1

        elif char == "(":
            tokens.append(Token("LEFTPARENTHESIS"))
            i += 1

        elif char == ")":
            tokens.append(Token("RIGHTPARENTHESIS"))
            i += 1

        elif char == ";":
            tokens.append(Token("SEMICOLON"))
            i += 1

        elif char == "<":
            tokens.append(Token("LT"))
            i += 1

        elif char == ">":
            tokens.append(Token("GT"))
            i += 1

        else:
            raise Exception(f"Unknown character! -> {char}")
        
    return tokens
    
