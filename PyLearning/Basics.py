# # calculate imc

# weight = float(input("What is your weight ? "))
# height = int(input("what is your height ? "))
# bmi = round(weight / ((height/100) ** 2), 2)
# state = ""
# if bmi <18.5:
#     state = "underweight"
# elif bmi >= 18.5 and bmi <= 24.9:
#     state = "normal"
# else:
#     state = "overweight"

# print(f"Your imc is {bmi} and you are {state}! ")

# ----------------------------------------------------------------------------------------------------------------

# # tip calculator

# total = float(input("What was the total bill ? $"))
# tips = int(input("How much tip would you like to give (10, 12 or 15) ? "))
# people = int(input("How many people to split the bill ? "))
# bill = round((total + (tips/100 * total)) / people, 2)

# print(f"Each person should pay: ${bill}")

# ----------------------------------------------------------------------------------------------------------------

# Pizza delivery

# Prices = {"S": 15, "M": 20, "L": 25}
# Pep_Prices = {"S": 2, "M": 3, "L": 3}
# total = 0

# size = input("What size do you want (S, M or L) ? ").upper()
# pepper = input("Do you want pepper or no (Y or N) ? ").upper()
# extra_cheese = input("Do you want extra cheese (Y or N) ? ").upper()
# total += Prices[size]

# if pepper == "Y":
#     total += Pep_Prices[size]

# if extra_cheese == "Y":
#     total += 1

# print(f"Your pizza will cost ${total} !")

# ----------------------------------------------------------------------------------------------------------------

# # Treasure Island Game

# import random

# # Colors

# RED = "\033[31m"
# GREEN = "\033[32m"
# YELLOW = "\033[33m"
# CYAN = "\033[36m"
# LIGHTPINK = "\033[38;2;255;182;193m"
# RESET = "\033[0m"

# # Clear the line if user type wrong char

# def clear_last_line():
#     print("\033[A\033[K", end="")  # 1 ligne vers le haut + clear line

# # Check good char in the inputs

# def choice (prompt, valid_choices):
#     choice = input(prompt).lower()
#     while choice not in valid_choices:
#         clear_last_line()
#         choice = input(prompt).lower()
#     return choice

# # Main function for the game

# def Game():
#     print(CYAN + "Welcome to Treasure Island ! You need to find the treasure" + RESET)

#     #Winning_Door = random.choice(["r", "y", "b"])

#     L_or_R = choice(LIGHTPINK + "Where do you want to go ? Left(l) or right(r) ? " + RESET, ["l", "r"])
#     if L_or_R == "r":
#         return print(RED + "You lost" + RESET)
#     S_or_W = choice(LIGHTPINK + "Do you want to swim(s) or wait(w) ? Type s or w : " + RESET, ["s", "w"])
#     if S_or_W == "s":
#         return print(RED + "You lost" + RESET)
#     Door = choice(LIGHTPINK + "Which door do you want to open ? yellow(y), red(r) or blue(b) ? " + RESET, ["y", "r", "b"])
#     if Door == "y":
#         print(GREEN + "Congratulations you won the game ! " + RESET)
#     else:
#         print(RED + "You lost but nice try " + RESET)

# # To play the game again

# while True:
#     Game()
#     again = input(YELLOW + "Wanna play again ? (y/n) : " + RESET).lower()
#     if again != "y":
#         print("Goodbye !")
#         break


# ----------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------

import random

# Training with lists (adding, removing, manipulate lists etc)

colors = ["\033[1;32m", "\033[1;31m", "\033[0;35m"]
GREEN = "\033[1;32m"
RED = "\033[1;31m"
END = "\033[0m"
fruits = ["Apple","Banana","Peach","Mango","Raspberry","Strawberry"]

# print(GREEN + str(fruits) + END)

# fruits[1] = "Orange" --> Change value index 1

# Add in a list
# fruits.append("Carot")
# fruits.extend(["peeeach", "pineeeeapple"])
# fruits[1:1] = ["Tomato", "Laituce", "Chiken"]

# Delete in a list
# fruits.remove("Raspberry")
# fruits.pop(1)
# fruits.pop()
# fruits.clear()
# print(RED + str(fruits) + END)

for fruit in fruits:
    print(random.choice(colors) + fruit + END)