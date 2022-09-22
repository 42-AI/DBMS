import sys

from src.SQLprompt import SQLprompt
from src.Parsing.Parser import Parser
from src.Interpreter import Interpreter


def main():
    while True:
        command = SQLprompt()
        if (command in ["exit", "quit", "\q", "exit;", "quit;", "\q;"]):
            print("Bye")
            break
        try:
            parsingTree = Parser.parser(command)
            Interpreter.execute(parsingTree)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    sys.exit(main())