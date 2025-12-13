import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def add(n1, n2):
    return n1 + n2

def sous(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":sous,
    "*":mult,
    "/":div
}

def calculator():
    number1 = float(input("What is the first number ?: "))
    while True:
        print("+\n-\n*\n/\n")
        symbol = input("Pick an operation: ")
        number2 = float(input("What is the second number ?: "))
        result = operations[symbol](number1, number2)
        
        print(f"\n{number1} {symbol} {number2} = {result}\n")

        again = input(f"('q' to quit the programm) type 'y' to continue calculating with {result}, type 'n' to start a new calculation : ")
        if again == "y":
            number1 = result
        elif again == "n":
            False
            clear()
            return calculator()
        elif again == "q":
            break
