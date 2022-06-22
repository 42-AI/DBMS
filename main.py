import sys

import prompt_toolkit.keys

from SQLprompt import SQLprompt
from parser import Parser
from Interpreter import Interpreter
import signal
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

def ctrlC_handler(signal, frame):
    sys.exit(0)


def main():
    # signal.signal(signal.SIGINT, ctrlC_handler)
    while True:
        commande = SQLprompt()
        if (commande in ["exit", "quit", "\q", "exit;", "quit;", "\q;"]) or prompt_toolkit.keys.Keys.ControlC:
            print("Bye")
            break
        parsingTree = Parser.parser(commande)
        print("END RESULT:", parsingTree)
        Interpreter.execute(parsingTree)


if __name__ == "__main__":
    sys.exit(main())