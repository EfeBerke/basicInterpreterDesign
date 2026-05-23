from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
print(if 3 < 5 then 1 else 0 end);
print(if false then 100 else 200 end);
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)