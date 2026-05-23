from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

code = """
let add = fun(a, b) -> a + b end;
print(add(3, 4));
print(add(10, 20));

let square = fun(x) -> x * x end;
print(square(5));

let max = fun(a, b) -> if a > b then a else b end end;
print(max(3, 7));
print(max(10, 2));
"""

tokens = tokenize(code)
parser = Parser(tokens)
program = parser.parse_program()

env = Environment()

for statement in program:
    evaluate(statement, env)