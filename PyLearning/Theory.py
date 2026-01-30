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

# ----------------------------------------------------------------------------------------------------------------

# POO Python

# import turtle

# my_screen = turtle.Screen()

# michel = turtle.Turtle()
# michel.shape("turtle")
# michel.turtlesize(3, 3, 2)
# michel.color("green")

# # L
# michel.right(90)
# michel.forward(200)
# michel.left(90)
# michel.forward(100)

# # I
# michel.left(90)
# michel.forward(100)
# michel.penup()
# michel.forward(30)
# michel.pendown()
# michel.dot(10)
# michel.penup()
# michel.backward(30)
# michel.pendown()
# michel.backward(100)
# michel.right(90)

# # o
# michel.forward(50)
# michel.left(90)
# michel.forward(100)
# michel.right(90)
# michel.forward(100)
# michel.right(90)
# michel.forward(100)
# michel.right(90)
# michel.forward(100)
# michel.left(180)
# michel.forward(100)

# # N
# michel.forward(50)
# michel.left(90)
# michel.forward(100)
# michel.right(150)
# michel.forward(100)
# michel.left(150)
# michel.forward(100)
# michel.right(180)
# michel.forward(120)
# michel.left(90)

# # E
# michel.forward(50)
# michel.left(90)
# michel.forward(100)
# michel.right(90)
# michel.forward(50)
# michel.backward(50)
# michel.right(90)
# michel.forward(50)
# michel.left(90)
# michel.forward(50)
# michel.backward(50)
# michel.right(90)
# michel.forward(50)
# michel.left(90)
# michel.forward(50)

# # L
# michel.forward(50)
# michel.left(90)
# michel.forward(100)
# michel.backward(100)
# michel.right(90)
# michel.forward(100)

# michel.circle(20)

# print(michel)
# my_screen.exitonclick()

# ----------------------------------------------------------------------------------------------------------------

# from prettytable import from_csv, TableStyle
# from prettytable.colortable import ColorTable, Themes

# my_table = PrettyTable()
# with open("pingouins.csv", "r") as fp:
#     my_table = from_csv(fp)

# my_table.__class__ = ColorTable
# my_table.theme = Themes.HIGH_CONTRAST
# my_table.set_style(TableStyle.DOUBLE_BORDER)
# new_rows = []
# for row in my_table.rows:
#     row[1] = int(row[1])
#     row[3] = int(row[3])
#     new_rows.append(row)

# my_table.clear_rows()
# my_table.add_rows(new_rows)
# my_table = ColorTable(theme=Themes.HIGH_CONTRAST)
# my_table.field_names = ["Nom pingouin", "Age", "Habitation", "Enfant(s)"]
# my_table.add_row(["Pingu", 2, "Banquise", 4])
# my_table.add_row(["Noot", 8, "Eau", 0])
# my_table.add_row(["Michel", 40, "terre", 12])
# my_table.align["Nom pingouin"] = "l"
# my_table.align["Enfant(s)"] = "r"

# print(my_table)
# print(my_table.get_string(sortby="Age"))

# ----------------------------------------------------------------------------------------------------------------

# class Chien:
#     def __init__(self, nom, race):
#         self.nom = nom
#         self.race = race

#     def abboyer(self):
#         return f"{self.nom} dit :Ouaf"

#     def dog(self):
#         return f"{self.nom} est une {self.race} !"

# class chat(Chien):
#     def __init__(self, nom, race):
#         self.nom = nom
#         self.race = race
#     def miaule(self):
#         return f"{self.nom} dit : Miaou !"

# mon_chien = Chien("pepito", "crapule")
# mon_chat = chat("Nyxie", "Queen")
# print(mon_chien.dog())
# print(mon_chat.dog())

# ----------------------------------------------------------------------------------------------------------------

# class Humain:
#     """
#     Classe des êtres humains
#     """

#     humain_crees = 0

#     def __init__(self, nom, age=1):
#         print("Salut")
#         self.prenom = nom
#         self.age = age
#         Humain.humain_crees += 1

# h1 = Humain("Pignu")
# h2 = Humain("NOOT")


# print(h1.prenom)
# print(h1.age)
# print(h1.humain_crees)

# ----------------------------------------------------------------------------------------------------------------

# class Humain:

#     lieu_habitation = "Terre"

#     def __init__(self, nom, age):
#         self.nom = nom
#         self.age = age

#     def parler(self, msg):
#         print("{} a dit : {}".format(self.nom, msg))

#     #méthode de classe
#     def changer_planete(cls, new_planet):
#         Humain.lieu_habitation = new_planet

#     changer_planete = classmethod(changer_planete)

#     #méthode statique
#     def definition():
#         print("L'humain est classé bla bla bla.")

#     definition = staticmethod(definition)

# h1 = Humain("lio", 24)

# print("Planète actuelle : {}".format(Humain.lieu_habitation))

# Humain.changer_planete("Zboub")

# print("Planète actuelle : {}".format(Humain.lieu_habitation))

# ----------------------------------------------------------------------------------------------------------------

# class Smartphone:
#     stock_total = 0

#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#         self.__class__.stock_total += 1

#     def add_promo(self, remise):
#         self.price -= remise

#     @classmethod
#     def print_stock(cls):
#         print(f"Stock total : {__class__.stock_total}")

#     @staticmethod
#     def imei_validate(imei):
#         return len(str(imei)) == 15

# Phone1 = Smartphone("Iphone", 1000)
# Phone2 = Smartphone("Samsung", 800)

# print("Price before : {}".format(Phone1.price))
# Phone1.add_promo(100)
# print("Price after : {}".format(Phone1.price))
# Smartphone.print_stock(Smartphone)
# print(Phone1.imei_validate(1234567891928223))

# ----------------------------------------------------------------------------------------------------------------

# from prettytable import PrettyTable
# from prettytable.colortable import ColorTable, Themes

# def add_tic(nbr):
#     s = str(nbr)
#     result = ""
#     count = 0

#     for digit in reversed(s):
#         if count == 3:
#             result += "'"
#             count = 0
#         result += digit
#         count += 1
#     return result[::-1]

# table = PrettyTable()
# table = ColorTable(theme=Themes.HIGH_CONTRAST)
# class Ferrari :
#     shipping_fees = 5000

#     def __init__(self, model, factory_price):
#         self.model = model
#         self.factory = factory_price
    
#     def get_total_price(self):
#         return self.factory + __class__.shipping_fees
    
#     @classmethod
#     def set_global_fees(cls, new_amount):
#         __class__.shipping_fees = new_amount
    
#     @staticmethod
#     def is_classic_color(color):
#         return color == "red" or color == "yellow"
    
# fefe1 = Ferrari("F40", 1500000)
# fefe2 = Ferrari("812 Superfast", 500000)

# Ferrari.set_global_fees(20000)
# fefe1_color = Ferrari.is_classic_color("red")
# fefe2_color = Ferrari.is_classic_color("blue")

# table.field_names = ["Model", "Price", "Total Price", "Classic color"]
# table.add_row([fefe1.model, add_tic(fefe1.factory), add_tic(fefe1.get_total_price()), fefe1_color])
# table.add_row([fefe2.model, add_tic(fefe2.factory), add_tic(fefe2.get_total_price()), fefe2_color])
# table.align["Model"] = "l"
# table.align["Price"] = "c"
# table.align["Total Price"] = "c"
# table.align["Classic color"] = "r"

# print(table)

# ----------------------------------------------------------------------------------------------------------------

# from turtle import Turtle, Screen
# import turtle
# import random

# turtle.colormode(255)

# Michel = Turtle()
# Michel.shape("turtle")
# Michel.pencolor()
# Michel.shapesize(3, 3, 3)
# Michel.pensize(10)
# Michel.speed(5)

# # draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         Michel.forward(100)
#         Michel.right(angle)

# for shape_side_n in range(3, 11):
#     Michel.pencolor(random.choice(colors))
#     draw_shape(shape_side_n)

# # random walk
# for s in range(100):
#     red = random.randint(0,255)
#     blue = random.randint(0,255)
#     green = random.randint(0,255)

#     Michel.pencolor(red, green, blue)
#     Michel.forward(100)
#     angles = [0,90,180,270]
#     Michel.setheading(random.choice(angles))

# #Spyrograph

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

#     return (r, g, b)

# def draw_spirograph(size_gap):
#     for _ in range(int(360 / size_gap)):
#         Michel.pencolor(random_color())
#         Michel.circle(100)
#         Michel.setheading(Michel.heading() + size_gap)

# draw_spirograph(5)




# import colorgram

# colors = colorgram.extract('hirst.jpg', 10)
# new = []
# for i in range(10):
#     first_color = colors[i]
#     rgb = first_color.rgb
#     red = rgb[0]
#     new.append((rgb[0], rgb[1], rgb[2]))
# print(new)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# for _ in range(10):
#     Michel.dot(20, random.choice(rgb_colors))
#     Michel.penup()
#     Michel.forward(50)


# screen = Screen()
# screen.setworldcoordinates(-100, -100, 100, 100)
# screen.exitonclick()


# ----------------------------------------------------------------------------------------------------------------
