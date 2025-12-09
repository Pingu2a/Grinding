Prices = {"S": 15, "M": 20, "L": 25}
Pep_Prices = {"S": 2, "M": 3, "L": 3}
total = 0

size = input("What size do you want (S, M or L) ? ").upper()
pepper = input("Do you want pepper or no (Y or N) ? ").upper()
extra_cheese = input("Do you want extra cheese (Y or N) ? ").upper()
total += Prices[size]

if pepper == "Y":
    total += Pep_Prices[size]

if extra_cheese == "Y":
    total += 1

print(f"Your pizza will cost ${total} !")