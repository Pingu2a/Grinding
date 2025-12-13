import random
import os

# Colors

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# Clearing the terminal

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Lists for the hangman stages and for the 20 animals
def Hang():
    hangman_stages = [
        """
        ------
        |    |
        |
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        --------
        """
    ]

    animals = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","bear","wolf","fox","rabbit","horse","cow","sheep","goat","pig","deer","kangaroo","penguin"]

    # Main game function

    def Game():
        print("Welcome to the Hangman game ! ")

    # Creating the main variables

        secret_word = random.choice(animals)
        blank = ["-"] * len(secret_word)
        life = 6
        wrong_letters = []

    # This loop check the letter entered, if this letter is in the secret word or if not.

        while True:

            print (f"Secret Word : {"".join(blank)}")
            letter = input("Type a letter to check if she's in the word : ")
            if len(letter) != 1 or not letter.isalpha():
                print("❌ Please enter only ONE letter.")
                continue
            if letter in blank or letter in wrong_letters:
                print("You already tried this letter!")
                continue
            if letter in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == letter:
                        blank[i] = letter
            else:
                life -= 1
                wrong_letters.append(letter)
            clear()
            mistakes = 6 - life

    # Printing the game for the user

            print(hangman_stages[mistakes])
            print("wrong letters : " + "".join(wrong_letters))
            print("".join(blank))
            print(f"Your life : {life}")

    # First if, is for the winning case, the second one if the user lose the game

            if secret_word == "".join(blank):
                finalWord = "".join(blank)
                clear()
                print(GREEN + f"You just found the word : {finalWord} !" + RESET)
                break
            elif mistakes == 6:
                clear()
                print(RED + "Oh no you lost :( \n" + RESET)
                print(f"The word was : {secret_word}")
                break

    # While loop for replay

    while True:
        Game()

        again = input(YELLOW + "\nDo you want to play again ? y/n : " + RESET)
        clear()
        if again != "y":
            print("Thanks for playing ! \n")
            break