weight = float(input("What is your weight ? "))
height = int(input("what is your height ? "))
bmi = round(weight / ((height/100) ** 2), 2)
state = ""
if bmi <18.5:
    state = "underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    state = "normal"
else:
    state = "overweight"

print(f"Your imc is {bmi} and you are {state}! ")