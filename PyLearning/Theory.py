# Training with random module


# import random


# print(random.randrange(0, 11, 2))
# print(random.randint(0, 11))
# print(round(random.random(), 2))

# list = ["Dog", "Cat", "Monkey", "Penguin", "Bear"]
# print(random.choice(list))
# print(random.choice(list[2]))
# print(random.choices(list, k=2))

# ----------------------------------------------------------------------------------------------------------------

# import random

# Training with lists (adding, removing, manipulate lists etc)

# colors = ["\033[1;32m", "\033[1;31m", "\033[0;35m"]
# GREEN = "\033[1;32m"
# RED = "\033[1;31m"
# END = "\033[0m"
# fruits = ["Apple","Banana","Peach","Mango","Raspberry","Strawberry"]

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

# for fruit in fruits:
#     print(random.choice(colors) + fruit + END)

# if "Apple" in fruits:
#     print(RED + "Yeah Apple is in the list ! " + END)

# print(len(fruits))

# ----------------------------------------------------------------------------------------------------------------

# Training loops etc

# fruits = ["apple", "pineapple", "mango", "Grapes"]
# var = 0
# for fr in fruits:
#     print(f"{fr} : {var}")
#     var += 1

# nbr = [137, 482, 915, 204, 653, 781, 329, 576, 844, 290]

# value = nbr[-1]
# for n in nbr:
#     if n < value:
#         value = n

# print(max(nbr))
# print(min(nbr))
# print(value)

# for i in range(10, 0, -2):
#     print(f"Noot Noot : {i}")

# lst = list(range(5))
# print(lst)

# def FizzBuzz():
#     lst = ["Fizz", "Buzz", "FizzBuzz"]
#     for nbr in range(1, 101):
#         if nbr % 3 == 0 and nbr % 5 == 0:
#             print(lst[2])
#         elif nbr % 3 == 0:
#             print(lst[0])
#         elif nbr % 5 == 0:
#             print(lst[1])
#         else:
#             print(nbr)

# FizzBuzz()