import random
from utils.input_utils import isint, y_or_n, clear, GREEN, LIGHTPINK, RED, RESET

def pwd():
    #Functions to encrypt the password

    def isXOR(txt, encrypt):
        return ''.join(chr(ord(c) ^ encrypt) for c in txt)
    def encrypt(pwd):
        return isXOR(pwd, 42)

    # Lists to use to create the new password
    while True:
        LETTERS = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        NUMBERS = ["0123456789"]
        SYMBOLS = ["!@#$%^&*"]
        password = []

        # Asking the user how many letters, numbers, symbols he wants

        print ("Welcome to the PWD Generator !!\n")
        nb_letters = isint("How many letters would you like in your pwd ? : ")
        nb_numbers = isint("How many numbers would you like in your pwd ? : ")
        nb_symbols = isint("How many symbols would you like in your pwd ? : ")

        #conditions and addind to empty list letters, symbols and numbers

        for i in range(nb_letters):
            password += random.choice(LETTERS[0])
        for j in range(nb_numbers):
            password += random.choice(NUMBERS[0])
        for k in range(nb_symbols):
            password += random.choice(SYMBOLS[0])

        # Shuffle the new password to have a real password

        random.shuffle(password)
        Final = "".join(password)

        # Encrypt the password with XOR method

        encrypted = encrypt(Final)
        print(f"\n{LIGHTPINK}Here is your password encrypted : {RESET}{RED}{encrypted}{RESET}\n")

        # Asking the used if he wants to see the real password  

        SeePwd = input("Press 'y' to decrypt ! ")
        if SeePwd == "y":
            Final = encrypt(encrypted)
            print(f"\n{LIGHTPINK}Your password is : {RESET}{GREEN}{Final}{RESET} \n")
        
        again = y_or_n("Do you want to generate another password ? (y/n): ")
        if again == "y":
            clear()
        else:
            break