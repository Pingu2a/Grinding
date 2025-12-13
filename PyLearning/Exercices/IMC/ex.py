from utils.input_utils import y_or_n, clear, isint, GREEN, LIGHTPINK, RED, RESET



def imcCalc():
    while True:
        weight = isint("What is your weight (kg)? ")
        height = isint("what is your height (cm)? ")
        bmi = round(weight / ((height/100) ** 2), 2)
        state = ""
        if bmi <18.5:
            state = f"{RED}underweight{RESET}"
        elif bmi >= 18.5 and bmi <= 24.9:
            state = f"{GREEN}normal{RESET}"
        else:
            state = f"{RED}overweight{RESET}"

        print(LIGHTPINK + f"\nYour imc is {bmi} and you are {state}! \n" + RESET)

        again = y_or_n("Do you want to calculate again ? (y/n): ")
        if again == "y":
            clear()
        else:
            return