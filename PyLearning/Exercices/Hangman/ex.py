import random
from utils.input_utils import RED, GREEN, YELLOW, RESET, clear


# Lists for the hangman stages and for the 20 animals
def Hang():
    HANGMAN_STAGES = [
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

    ANIMALS = ["cat","dog","lion","tiger","elephant","giraffe","zebra","monkey","bear","wolf","fox","rabbit","horse","cow","sheep","goat","pig","deer","kangaroo","penguin"]

    # Main game function

    def Game():
        print("Welcome to the Hangman game ! \n")

    # Creating the main variables

        secret_word = random.choice(ANIMALS)
        blank = ["-"] * len(secret_word)
        life = 6
        wrong_letters = []

    # This loop check the letter entered, if this letter is in the secret word or if not.

        while True:

            print (f"Secret Word : {"".join(blank)}")
            letter = input("Type a letter to check if it is in the word : ")
            if len(letter) != 1 or not letter.isalpha():
                print(RED + "\nPlease enter only ONE letter.\n" + RESET)
                continue
            if letter in blank or letter in wrong_letters:
                print(RED + "\nYou already tried this letter!\n" + RESET)
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

            print(HANGMAN_STAGES[mistakes])
            print("wrong letters : " + "".join(wrong_letters) + "\n")
            print("".join(blank) + "\n")
            print(f"Your life : {life}\n")

    # First if, is for the winning case, the second one if the user lose the game

            if secret_word == "".join(blank):
                finalWord = "".join(blank)
                clear()
                print(GREEN + f"\nYou just found the word : {finalWord} !\n" + RESET)
                break
            elif mistakes == 6:
                clear()
                print(RED + "Oh no you lost :( \n" + RESET)
                print(f"\nThe word was : {secret_word}\n")
                break

    # While loop for replay

    while True:
        Game()

        again = input(YELLOW + "\nDo you want to play again ? y/n : " + RESET)
        clear()
        if again != "y":
            print("Thanks for playing ! \n")
            break