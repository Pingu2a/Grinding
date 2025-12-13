import random

def pwd():
    #Functions to encrypt the password

    def isXOR(txt, encrypt):
        return ''.join(chr(ord(c) ^ encrypt) for c in txt)
    def encrypt(pwd):
        return isXOR(pwd, 42)

    # Lists to use to create the new password

    letters = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    numbers = ["0123456789"]
    symbols = ["!@#$%^&*"]
    password = []

    # Asking the user how many letters, numbers, symbols he wants

    print ("Welcome to the PWD Generator !!")
    nb_letters = int(input("How many letters would you like in your pwd ? : "))
    nb_numbers = int(input("How many numbers would you like in your pwd ? : "))
    nb_symbols = int(input("How many symbols would you like in your pwd ? : "))

    #conditions and addind to empty list letters, symbols and numbers

    for i in range(nb_letters):
        password += random.choice(letters[0])
    for j in range(nb_numbers):
        password += random.choice(numbers[0])
    for k in range(nb_symbols):
        password += random.choice(symbols[0])

    # Shuffle the new password to have a real password

    random.shuffle(password)
    Final = "".join(password)

    # Encrypt the password with XOR method

    encrypted = encrypt(Final)
    print(f"Here is your password encrypted : {encrypted}")

    # Asking the used if he wants to see the real password  

    SeePwd = input("Press 'y' to decrypt ! ")
    if SeePwd == "y":
        Final = encrypt(encrypted)
        print(f"Your password is : {Final} ")