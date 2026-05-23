from lexer import tokenize
from parser import Parser
from evaluator import evaluate

code = "(3 + 4) * 2"

tokens = tokenize(code)

parser = Parser(tokens)

tree = parser.parse_expression()

result = evaluate(tree)

print(result)