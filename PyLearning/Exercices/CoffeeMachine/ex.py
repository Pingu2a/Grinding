
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
    "coffee" : 70
}

machine_money = 0

def money_putted(usr_money):
    money = [0.25, 0.10, 0.05, 0.01]
    usr_total = 0
    for i in range(len(usr_money)):
        usr_total += usr_money[i] * money[i]
    return round(usr_total, 2)

def machine_report():
    print(f"Water : {ressources['water']}ml")
    print(f"Milk : {ressources['milk']}ml")
    print(f"Coffee : {ressources['coffee']}g")

def coffee(coffee):
    drink = COFFEES[coffee]
    for item in drink["ingredients"]:
        ressources[item] -= drink["ingredients"][item]
    return drink["price"]


def coffee_machine():
    print("Welcome to the coffee machine !")
    while True:
        usr_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if usr_choice == 'report':
            machine_report()
        else:
            coffee_chosen = coffee(usr_choice)
            break
    print("Please insert coins: ")
    coin_names = ["quarters", "dimes", "nickles", "pennies"]
    usr_money = []
    for coin in coin_names:
        usr_money.append(int(input(f"How many {coin} : ")))

    total_money = money_putted(usr_money)
    money_back = round(total_money - coffee_chosen, 2)

    print(f"Total inserted : {total_money}$")
    print(f"Café : {usr_choice} prix : {COFFEES[usr_choice]["price"]}")
    print(f"Total restant : {money_back}$")


coffee_machine()