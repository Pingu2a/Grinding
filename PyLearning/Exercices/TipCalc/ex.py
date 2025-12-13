def tipCalc():
    total = float(input("What was the total bill ? $"))
    tips = int(input("How much tip would you like to give (10, 12 or 15) ? "))
    people = int(input("How many people to split the bill ? "))
    bill = round((total + (tips/100 * total)) / people, 2)

    return print(f"Each person should pay: ${bill}")