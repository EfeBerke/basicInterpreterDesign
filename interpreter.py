from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
print(true and false);
print(true or false);
print(not false);
print(3 < 5 and 10 == 10);
print(false or 2 < 3);
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)