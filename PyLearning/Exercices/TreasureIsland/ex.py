import random

# Colors

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
LIGHTPINK = "\033[38;2;255;182;193m"
RESET = "\033[0m"

# Clear the line if user type wrong char

def clear_last_line():
    print("\033[A\033[K", end="")

# Check good char in the inputs

def choice(prompt, valid_choices):
    choice = input(prompt).lower()
    while choice not in valid_choices:
        clear_last_line()
        choice = input(prompt).lower()
    return choice

# Main function for the game
def Treasure():
    def Game():
        print(CYAN + "Welcome to Treasure Island ! You need to find the treasure" + RESET)

        #Winning_Door = random.choice(["r", "y", "b"])

        L_or_R = choice(LIGHTPINK + "Where do you want to go ? Left(l) or right(r) ? " + RESET, ["l", "r"])
        if L_or_R == "r":
            return print(RED + "You lost" + RESET)
        S_or_W = choice(LIGHTPINK + "Do you want to swim(s) or wait(w) ? Type s or w : " + RESET, ["s", "w"])
        if S_or_W == "s":
            return print(RED + "You lost" + RESET)
        Door = choice(LIGHTPINK + "Which door do you want to open ? yellow(y), red(r) or blue(b) ? " + RESET, ["y", "r", "b"])
        if Door == "y":
            print(GREEN + "Congratulations you won the game ! " + RESET)
        else:
            print(RED + "You lost but nice try " + RESET)

    # To play the game again

    while True:
        Game()
        again = input(YELLOW + "Wanna play again ? (y/n) : " + RESET).lower()
        if again != "y":
            print("Goodbye !")
            break
