from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
let a = true;
let b = false;
print(a);
print(b);
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)