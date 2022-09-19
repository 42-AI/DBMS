from src.Parsing.Parser import Parser
from src.Interpreter import Interpreter
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from datetime import datetime

bindings = KeyBindings()


@bindings.add('c-c')
@bindings.add('c-d')
def _(event):
    exit(0)

def writeInHistory(text):
    with open('.history.txt', 'a') as f:
        f.write('\n# ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + "\n" +
                "+" + text + "\n")

def multiLinePrompt(text):
    buffer = str(text)
    while not buffer.endswith(";"):
        text = prompt("  -> ", history=FileHistory('.buffer_hist.txt'), key_bindings=bindings)
        if not (type(text) is str):
            return ("exit")
        if not str.isspace(text) and len(text) > 0:
            buffer += " " + text.strip(" ")
    writeInHistory(buffer)
    return buffer

def parsText(text):
    parsingTree = Parser.parser(text)
    Interpreter.execute(parsingTree)

def SQLprompt():
    text = prompt("dbms> ", history=FileHistory('.history.txt'), key_bindings=bindings)
    # print(type(text))
    if not (type(text) is str) or (text in ["exit", "quit", "\\q"]):
        return text
    else:
        return multiLinePrompt(text)