# Efe Berke Vatansever - 2025402006 - CMPE260 Basic Interpreter Project
from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

import sys # for file inputs

test_file = sys.argv[1]

with open(test_file, "r") as test:
    code = test.read()

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)