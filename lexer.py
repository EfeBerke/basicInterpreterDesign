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

        else:
            raise Exception(f"Unknown character! -> {char}")
        
    return tokens
    
