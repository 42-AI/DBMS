import sys
from SQLprompt import SQLprompt
from parser import Parser
from Interpreter import Interpreter
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

def main():
    while True:
        commande = SQLprompt()
        if (commande in ["exit", "quit", "\q", "exit;", "quit;", "\q;"]):
            print("Bye")
            break
        parsingTree = Parser.parser(commande)
        # print("END RESULT:", parsingTree)
        Interpreter.execute(parsingTree)


if __name__ == "__main__":
    sys.exit(main())