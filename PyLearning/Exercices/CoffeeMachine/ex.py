from utils.input_utils import GREEN, LIGHTPINK, RED, RESET

COFFEES = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 2.5
    },
    "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 3
    },
}
ressources = {
    "milk" : 500,
    "water" : 400,
    "coffee" : 70,
    "money" : 0
}

machine_money = 0

def money_putted(usr_money):
    money = [0.25, 0.10, 0.05, 0.01]
    usr_total = 0
    for i in range(len(usr_money)):
        usr_total += usr_money[i] * money[i]
    return round(usr_total, 2)

def machine_report():
    print("--------------------------------")
    print(f"Water : {ressources['water']}ml")
    print(f"Milk : {ressources['milk']}ml")
    print(f"Coffee : {ressources['coffee']}g")
    print(f"Money : {ressources['money']}$")
    print("--------------------------------\n")


def coffee(coffee):
    drink = COFFEES[coffee]
    for item in drink["ingredients"]:
        ressources[item] -= drink["ingredients"][item]
    return drink["price"]

def check_resources(usr_choice):
    ingredients_needed = COFFEES[usr_choice]["ingredients"]
    for item in ingredients_needed:
        if ingredients_needed[item] > ressources[item]:
            print(f"\n{RED}Sorry, there is not enough {item}.{RESET}\n")
            return False
    return True

def refill():
    ressources["water"] += int(input("Water : "))
    ressources["milk"] += int(input("Milk : "))
    ressources["coffee"] += int(input("Coffee : "))

def coffee_machine():
    print("Welcome to the coffee machine !")
    while True:
        usr_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if usr_choice == "off":
            break
        if usr_choice == 'report':
            machine_report()
            continue
        if usr_choice == 'refill':
            refill()
            continue
        if usr_choice not in COFFEES:
            print(f"{RED}\nInvalid choice, please insert a good one.\n{RESET}")
            continue

        if not check_resources(usr_choice):
            continue
        print("\n----- Please insert coins -----\n ")
        coin_names = ["quarters", "dimes", "nickles", "pennies"]
        usr_money = []
        for coin in coin_names:
            usr_money.append(int(input(f"How many {coin} : ")))

        total_money = money_putted(usr_money)

        price = COFFEES[usr_choice]["price"]

        if total_money < price:
            print(f"Sorry that's not enought money. {total_money:.2f}$ refunded.")
        else:
            coffee_chosen = coffee(usr_choice)
            money_back = round(total_money - coffee_chosen, 2)
            ressources["money"] = total_money - money_back

            print("-------------------------------")
            print(f"Total inserted : {LIGHTPINK}{total_money:.2f}${RESET}")
            print(f"{usr_choice} price : {LIGHTPINK}{COFFEES[usr_choice]["price"]:.2f}${RESET}")
            print(f"Here is {LIGHTPINK}{money_back:.2f}${RESET} in change.")
            print(f"{GREEN}Here is your {usr_choice} Enjoy !{RESET}")
            print("-------------------------------")
