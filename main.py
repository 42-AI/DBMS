import sys

from SQLprompt import SQLprompt
from parser import Parser
from Interpreter import Interpreter


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