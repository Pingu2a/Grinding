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