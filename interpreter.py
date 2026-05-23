from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
print(3 < 5);
print(10 == 10);
print(7 != 2);
print(5 >= 5);
print(8 <= 3);
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)