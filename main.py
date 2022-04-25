import sys
from parser import parser
from Interpreter import Interpreter

def main():
    while True:
        text = input("dbms> ")
        if (text in ["exit", "quit", "\q"]):
            print("Bye")
            break
        print(text)
        parsingTree = parser(text)
        print("END RESULT:", parsingTree)
        Interpreter.execute(parsingTree)


if __name__ == "__main__":
    sys.exit(main())