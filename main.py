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
        parsingTree = Parser.parser(command)
        # print("END RESULT:", parsingTree)
        Interpreter.execute(parsingTree)


if __name__ == "__main__":
    sys.exit(main())