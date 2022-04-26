import sys
from parser import Parser
from Interpreter import Interpreter
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

def main():
    while True:
        text = prompt("dbms> ", history=FileHistory('.history.txt'),)
        if (text in ["exit", "quit", "\q"]):
            print("Bye")
            break
        print(text)
        parsingTree = Parser.parser(text)
        print("END RESULT:", parsingTree)
        Interpreter.execute(parsingTree)


if __name__ == "__main__":
    sys.exit(main())