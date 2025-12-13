from utils.input_utils import GREEN, YELLOW, RESET, clear

def SecretAuction():
    print("Welcome to the secret auction !")

    # ask user name and bid

    bid = {}
    def highestB(bids):
        winner = ""
        highest_bid = 0

        for name, bid in bids.items():
            if bid > highest_bid:
                winner = name
                highest_bid = bid
        return print(GREEN + f"The winner is : {winner} with a price of {highest_bid}$ ! \n" + RESET)


    def printBidders(bid):
        for key, val in bid.items():
            print(f"{key} : {val}$")

    while True:
        name = input("What is your name ? : ")
        price = int(input("What is your bid ? : $"))
        bid[name] = price
        toContinue = input(YELLOW + "Are there any other bidders ? y/n : " + RESET).lower()
        clear()
        if toContinue == "n":
            highestB(bid)
            print("Bidders : \n")
            printBidders(bid)
            break
