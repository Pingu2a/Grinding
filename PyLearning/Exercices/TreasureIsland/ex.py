from utils.input_utils import CYAN, RED, GREEN, YELLOW, LIGHTPINK, RESET

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
        print(CYAN + "Welcome to Treasure Island ! You need to find the treasure\n" + RESET)

        #Winning_Door = random.choice(["r", "y", "b"])

        L_or_R = choice(LIGHTPINK + "Where do you want to go ? Left(l) or right(r) ? " + RESET, ["l", "r"])
        if L_or_R == "r":
            return print(RED + "\nYou lost\n" + RESET)
        S_or_W = choice(LIGHTPINK + "Do you want to swim(s) or wait(w) ? Type s or w : " + RESET, ["s", "w"])
        if S_or_W == "s":
            return print(RED + "\nYou lost\n" + RESET)
        Door = choice(LIGHTPINK + "Which door do you want to open ? yellow(y), red(r) or blue(b) ? " + RESET, ["y", "r", "b"])
        if Door == "y":
            print(GREEN + "\nCongratulations you won the game ! \n" + RESET)
        else:
            print(RED + "\nYou lost but nice try \n" + RESET)

    # To play the game again

    while True:
        Game()
        again = input(YELLOW + "Wanna play again ? (y/n) : " + RESET).lower()
        if again != "y":
            print("\nGoodbye !\n")
            break
