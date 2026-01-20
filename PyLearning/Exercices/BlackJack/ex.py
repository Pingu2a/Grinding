import random
from utils.input_utils import y_or_n
cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10,
    "A": 11
}
signs = ["♣", "♠", "♥", "♦"]

def draw_card():
    rank = random.choice(list(cards.keys()))
    sign = random.choice(signs)
    return rank + sign

def hand_value(hand, cards_values):
    total = 0
    aces = 0

    for card in hand:
        rank = card[:-1]
        total += cards_values[rank]
        if rank == "A":
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def winner(computer_total, user_total):
    if user_total > 21:
        return "computer"
    if computer_total > 21:
        return "user"
    if user_total > computer_total:
        return "user"
    if computer_total > user_total:
        return "computer"
    return "draw"

def play_one_game(money):
    print("\n==============================")
    print("Welcome to the BlackJack Game")
    print("Your money:", money, "$")

    bet = int(input("How much money do you want to bet ? : $"))

    if bet <= 0:
        print("Bet must be > 0")
        return money

    if bet > money:
        print("You don't have enough money!")
        return money

    money -= bet

    ComputerCards = [draw_card(), draw_card()]
    UserCards = [draw_card(), draw_card()]

    print("\n--- Start ---")
    print("Computer's cards :", f"{ComputerCards[0]} | ??")
    print("Your cards :", " | ".join(UserCards))

    user_total = hand_value(UserCards, cards)
    computer_total = hand_value(ComputerCards, cards)

    if user_total == 21:
        print("Blackjack ! you win")
        money += bet * 2.5
    else:
        # Tour du joueur
        while True:
            if user_total > 21:
                print("\nBUST! You went over 21")
                break

            pull = y_or_n("\nDo you want to pull a card ? (y/n) ")

            if pull == "n":
                break

            UserCards.append(draw_card())
            print("Your cards :", " | ".join(UserCards))

        # Computer taking card only if user didn't bust
        if hand_value(UserCards, cards) <= 21:
            if computer_total == 21:
                print("Computer blackJack ! you lost")
            else:
                while hand_value(ComputerCards, cards) < 17:
                    ComputerCards.append(draw_card())

    # Reveal + result
    print("\n--- Final hands ---")
    print("Computer's cards :", " | ".join(ComputerCards))
    print("Your cards :", " | ".join(UserCards))

    user_total = hand_value(UserCards, cards)
    computer_total = hand_value(ComputerCards, cards)

    w = winner(computer_total, user_total)

    if w == "user":
        print("\nYou won!")
        money += bet * 2 
    elif w == "draw":
        print("\nDraw ")
        money += bet 
    else:
        print("\nComputer won")

    print(f"Computer: {computer_total} | You: {user_total}")
    print("Your money is now:", money, "$")

    return money
def BlackJack():
    money = 100

    while True:
        if money <= 0:
            print("\nYou have no money left... Game over!")
            break

        money = play_one_game(money)

        again = y_or_n("\nDo you want to play again ? (y/n) ")
        if again == "n":
            print("\nBye ")
            break
if __name__ == "__main__":
    BlackJack()
