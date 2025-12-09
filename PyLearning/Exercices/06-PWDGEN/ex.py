import random

def isXOR(txt, encrypt):
    return ''.join(chr(ord(c) ^ encrypt) for c in txt)
def encrypt(pwd):
    return isXOR(pwd, 42)

letters = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
numbers = ["0123456789"]
symbols = ["!@#$%^&*"]
password = []

print ("Welcome to the PWD Generator !!")
nb_letters = int(input("How many letters would you like in your pwd ? : "))
nb_numbers = int(input("How many numbers would you like in your pwd ? : "))
nb_symbols = int(input("How many symbols would you like in your pwd ? : "))

for i in range(nb_letters):
    password += random.choice(letters[0])
for j in range(nb_numbers):
    password += random.choice(numbers[0])
for k in range(nb_symbols):
    password += random.choice(symbols[0])

random.shuffle(password)
Final = "".join(password)

encrypted = encrypt(Final)
print(f"Here is your password encrypted : {encrypted}")

SeePwd = input("Press 'y' to decrypt ! ")
if SeePwd == "y":
    Final = encrypt(encrypted)
    print(f"Your password is : {Final} ")
