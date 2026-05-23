from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
let x = 10;
print(x+5);
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)