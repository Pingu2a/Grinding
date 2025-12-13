from utils.input_utils import LIGHTPINK, RED,  RESET, y_or_n, clear, ask_number

TIP = [10, 12, 15]



def tipCalc():
    while True:
        total = ask_number("What was the total bill ? $")
        while True:
            tips = ask_number("How much tip would you like to give (10, 12 or 15) ? ")
            if tips in TIP:
                break
            print(RED + "\nPlease enter the good tip ! \n" + RESET)

        people = ask_number("How many people to split the bill ? ")
        bill = round((total + (tips/100 * total)) / people, 2)

        print(LIGHTPINK + f"\nEach person should pay: ${bill}\n" + RESET)

        again = y_or_n("Do you want to calculate the bill again ? (y/n): ")
        if again == "y":
            clear()
        else:
            break