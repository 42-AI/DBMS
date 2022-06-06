from parser import Parser
from Interpreter import Interpreter
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from datetime import datetime

def writeInHistory(text):
    with open('.history.txt', 'a') as f:
        f.write('\n# ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "\n" +
                "+" + text + "\n")

def multiLinePrompt(text):
    buffer = str(text)
    while not buffer.endswith(";"):
        text = prompt("  -> ", history=FileHistory('.buffer_hist.txt'), )
        if not str.isspace(text) and len(text) > 0:
            buffer += " " + text.strip(" ")
    writeInHistory(buffer)
    return buffer

def parsText(text):
    parsingTree = Parser.parser(text)
    Interpreter.execute(parsingTree)

def SQLprompt():
    text = prompt("dbms> ", history=FileHistory('.history.txt'), )
    if (text in ["exit", "quit", "\q"]) or str(text).lower().startswith("use"):
        return text
    else:
        return multiLinePrompt(text)