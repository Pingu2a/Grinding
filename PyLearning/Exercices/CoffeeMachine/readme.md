# Coffee machine

For this exercice, I had to create a coffe machine ! 

[Requirements PDF](../docs/Coffee+Machine+Program+Requirements.pdf)

Here is how it works:

- A dictionary contains the coffee recipes (Espresso, Latte, Cappuccino) and their prices.
- A resource dictionary tracks the current levels of water, milk, coffee, and money.
- The user can choose a drink, see a report of resources, refill the machine, or turn it off.
- The machine checks if it has enough ingredients before asking for money.
- Payments are processed using four types of coins: quarters, dimes, nickels, and pennies.
- If the user provides enough money, the drink is prepared, resources are deducted, and change is returned.

## Logic

**function coffee_machine**

This is the main function that runs the machine. It uses a while True loop to keep the machine running until the user types "off". It manages the flow of the program:
- Taking the user's order.
- Checking if the choice is valid.
- Verifying if there are enough resources using *check_resources*.
- Processing the payment if resources are sufficient.
- Calculating the change and serving the coffee using *coffee*.

**function money_putted**

This function takes a list of coins inserted by the user and calculates the total value in dollars.

**function check_resources**

This function compares the ingredients required for the chosen drink with the current ressources. It returns False and alerts the user if something is missing.

**function coffee**

This function performs the "brewing" action. It deducts the required ingredients from the machine's inventory and returns the price of the drink.

**function machine_report**

An admin function that prints the current status of all resources (Water, Milk, Coffee) and the total money earned by the machine.

**function refill**

Allows the user to manually add quantities to the water, milk, and coffee stocks.