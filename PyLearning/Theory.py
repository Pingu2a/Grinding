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

# ----------------------------------------------------------------------------------------------------------------


# def Until90(age):
#     return 4680 - (age * 52)

# left = Until90(63)
# print(f"You have {left} weeks left before reaching 90 years old ! \n")

# ----------------------------------------------------------------------------------------------------------------

# Love calculator

# def love(n1, n2):
#     names = (n1 + n2).upper()
#     Tword = "TRUE"
#     Lword = "LOVE"
#     count1 = 0
#     count2 = 0
#     for i in names:
#         for j in Tword:
#             if i == j:
#                 count1 += 1
#     for k in names:
#         for l in Lword:
#             if k == l:
#                 count2 += 1
#     print(f"Your love score : {count1}{count2}\n")

# love("Marge Simpson", "Omer Simpson")

# ----------------------------------------------------------------------------------------------------------------

# Dictionaries

# def eat():
#     return print("MIAM MIAM")
# Penguin = {
#     "name" : "Pingu",
#     "Age" : 12,
#     "family": {"dad": "papaNOOT", "mum": "mamaNOOT"},
#     "food" : ["fish", "ice"],
#     "eat": eat()
# }

# print(Penguin["Age"])
# print(Penguin["food"][0])
# print(Penguin["family"]["dad"] + "\n")

# Penguin["friend"] = "niit"
# Penguin["Age"] = 20

# print(Penguin)

# del Penguin["food"]

# print(Penguin)
# Penguin["eat"]

# for key, val in Penguin.items():
#     print(key," NOOT ", val)

# ----------------------------------------------------------------------------------------------------------------

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# grades = ["Outstanding", "Exceeds Exectations", "Acceptable", "Fail"]

# for student, score in student_scores.items():
#     if score >= 90:
#         print(f"Student name : {student} and his com : {grades[0]}")
#     elif score > 80 and score <= 90:
#         print(f"Student name : {student} and his com : {grades[1]}")
#     elif score > 70 and score <= 80:
#         print(f"Student name : {student} and his com : {grades[2]}")
#     elif score <= 70:
#         print(f"Student name : {student} and his com : {grades[3]}")

# ----------------------------------------------------------------------------------------------------------------

# Created the method .title() for fun :)

# def toUpper(txt):
#     """
#     This function can transform a str into a str with an uppercase at the begining and the rest of the text in lowercase
    
#     :param txt: text to transform
#     :return: return the result with the first letter in uppercase and the rest in lowercase
#     """
#     result = ""
#     i = 1
#     result += txt[0].upper()
#     while i < len(txt):
#         result += txt[i].lower()
#         i+=1
#     return result

# def toTitle(firstname, lastname):
#     all = toUpper(firstname) + " " + toUpper(lastname)
#     return print(all)

# toTitle("OMEr", "SimpSON")
# toTitle("omer", "simpson")
# toTitle("OMER", "SIMPSON")

# ----------------------------------------------------------------------------------------------------------------

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# print(is_prime(75))
# print(is_prime(1))
# print(is_prime(73))

# ----------------------------------------------------------------------------------------------------------------

# Modifying a global variable 
# Constant global variable must be in uppercase. The variable will not change

# PI = 3.14
# enemy = "Zombie"

# def change_enemy():
#     global enemy 
#     enemy = "Skeleton"
#     return enemy

# print(enemy)
# print(change_enemy())

# ----------------------------------------------------------------------------------------------------------------

# def test():
#     while True:
#         try:
#             age = int(input("How old are you ?"))
#             return age
#         except ValueError:
#             print("try again")

# age = test()
# if age > 18:
#     print("Majeur")

# ----------------------------------------------------------------------------------------------------------------

# try:
#     f = open("demofile.txt", "a")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

