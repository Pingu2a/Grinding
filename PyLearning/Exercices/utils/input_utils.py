import os

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
LIGHTPINK = "\033[38;2;255;182;193m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def y_or_n(message):
    while True:
        answer = input(message).lower()
        if answer in ("y", "n"):
            return answer
        print(RED + "\nPlease enter only 'y' or 'n'\n" + RESET)

def isint(message):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        print(RED + "\nPlease enter a valid integer\n" + RESET)

def ask_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(RED + "\nPlease enter a valid number\n" + RESET)