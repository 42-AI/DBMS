import sys
import select

from src.SQLprompt import SQLprompt
from src.Parsing.Parser import Parser
from src.Interpreter import Interpreter


def handle_commande(command):
    try:
        parsingTree = Parser.parser(command)
        Interpreter.execute(parsingTree)
    except Exception as e:
        print(f"Error: {e}")


def main():
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        command = ""
        for line in sys.stdin:
            command += line
            if ';' in command:
                handle_commande(command)
                command = ""
    else:
        while True:
            command = SQLprompt()
            if (command in ["exit", "quit", "\q", "exit;", "quit;", "\q;"]):
                print("Bye")
                break
            handle_commande(command)

if __name__ == "__main__":
    sys.exit(main())