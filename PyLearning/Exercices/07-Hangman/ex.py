import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

def Game():
    print("Welcome to the Hangman game ! ")

    secret_word = random.choice(animals)
    blank = ["-"] * len(secret_word)
    life = 6
    wrong_letters = []

    while True:

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
            # wrong_ltr(letter, wrong_letters)
            wrong_letters.append(letter)
        clear()
        mistakes = 6 - life
        print(hangman_stages[mistakes])
        print("wrong letters : " + "".join(wrong_letters))
        print("".join(blank))
        print(f"Your life : {life}")




        if secret_word == "".join(blank):
            finalWord = "".join(blank)
            print(f"You just found the word : {finalWord} !")
            break
        elif mistakes == 6:
            print("Oh no you lost :( ")
            print(f"The word was : {secret_word}")
            break

while True:
    Game()

    again = input("Do you want to play again ? y/n : ")
    clear()
    if again != "y":
        print("Thanks for playing ! ")
        break