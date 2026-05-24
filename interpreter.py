# Efe Berke Vatansever, 2025402006
from lexer import tokenize
from parser import Parser
from evaluator import evaluate
from environment import Environment

# for file inputs
import sys 

def main():
    if len(sys.argv) != 2:
        print("", file = sys.stderr)
        sys.exit(1)

    test_file = sys.argv[1]

    with open(test_file, "r") as test:
        code = test.read()

    tokens = tokenize(code)
    parser = Parser(tokens)
    program = parser.parse_program()

    env = Environment()

    for statement in program:
        evaluate(statement, env)

try:
    main()
    sys.exit(0)
except Exception as error:
    print(str(error), file=sys.stderr)
    sys.exit(1)