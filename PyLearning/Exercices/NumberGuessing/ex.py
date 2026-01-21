import random
from utils.input_utils import GREEN, RED, CYAN, RESET, y_or_n, clear, isint


def check_answer(user_guess, answer):
    if user_guess > answer:
        print("\nTo high.\n")
    elif user_guess < answer:
        print("\nTo low.\n")
    else:
        print(f"{GREEN}Congrats you won ! The number was {answer}{RESET}")
        return 1

def number_guessing():
    while True:
        NUMBER = random.randint(1,100)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

        attempts = 10 if difficulty == 'easy' else 5
        win = 0
        while attempts > 0 and win == 0:
            print(f"Attempts : {CYAN}{attempts}{RESET}")
            #user_number = int(input("type a number : "))
            user_number = isint("Typer a number : ")
            check_ans = check_answer(user_number, NUMBER)
            if check_ans == 1:
                win = 1
            attempts -= 1
        if attempts == 0:
            print(f"{RED}Oh no you lost :(\n{RESET}")
        again = y_or_n(f"{CYAN}Do you want to play again ? (y/n) : {RESET}")

        if again == 'y':
            clear()
        elif again == 'n':
            return