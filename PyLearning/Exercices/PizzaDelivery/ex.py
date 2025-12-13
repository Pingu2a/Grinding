from utils.input_utils import RED, LIGHTPINK, RESET, y_or_n, clear

def Pizza():
    PRICES = {"S": 15, "M": 20, "L": 25}
    PEPPER_PRICES = {"S": 2, "M": 3, "L": 3}
    while True:
        total = 0

        size = input("What size do you want (S, M or L) ? ").upper()
        if size not in PRICES:
            print(RED + "Invalid size !" + RESET)
            continue
        pepper = y_or_n("Do you want pepper or no (Y or N) ? ").upper()
        extra_cheese = y_or_n("Do you want extra cheese (Y or N) ? ").upper()
        total += PRICES[size]

        if pepper == "Y":
            total += PEPPER_PRICES[size]

        if extra_cheese == "Y":
            total += 1

        print(LIGHTPINK + f"\nYour pizza will cost ${total} !\n" + RESET)

        again = y_or_n("Do you want to order another pizza ? y/n : ").lower()
        if again == "y":
            clear()
        else:
            return