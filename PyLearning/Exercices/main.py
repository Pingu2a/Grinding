import Calculator.ex as calc
import IMC.ex as imc
import TipCalc.ex as tip
import PizzaDelivery.ex as pizz
import TreasureIsland.ex as treasure
import RockPaperScisors.ex as rpc
import PWDGEN.ex as passwd
import Hangman.ex as hangman
import SecretAuction.ex as secret

while True:
    print("Exercices :\n1: IMC\n2: Tip calculator\n3: Pizza Delivery\n4: Treasure Island\n5: Rock Paper Scisors\n6: Password Generator\
        \n7: Hangman\n8: Secret Auction\n9: Calculator")
    choice = int(input("\nChoose an exercice : "))

    if choice == 1:
        print("""
    ========================================
            ⚖️  IMC CALCULATOR  ⚖️
    ========================================
    """)
        imc.imcCalc()
    elif choice == 2:
        print("""
    ========================================
            💸  TIP CALCULATOR
    ========================================
    """)
        tip.tipCalc()
    elif choice == 3:
        print("""
    ========================================
            🍕  PIZZA DELIVERY  🍕
    ========================================
    """)
        pizz.Pizza()
    elif choice == 4:
        print("""
    ========================================
            🏝️  TREASURE ISLAND  🏝️
    ========================================
    """)
        treasure.Treasure()
    elif choice == 5:
        print("""
    ========================================
        ✊ 🖐️ ✌️  ROCK PAPER SCISSORS
    ========================================
    """)
        rpc.RPS()
    elif choice == 6:
        print("""
    ========================================
            🔐  PASSWORD GENERATOR
    ========================================
    """)
        passwd.pwd()
    elif choice == 7:
        print("""
    ========================================
                🎯  HANGMAN
    ========================================
    """)
        hangman.Hang()
    elif choice == 8:
        print("""
    ========================================
            💰  SECRET AUCTION
    ========================================
    """)
        secret.SecretAuction()
    elif choice == 9:
        print("""
    ========================================
                🧮  CALCULATOR
    ========================================
    """)
        calc.calculator()

    again = input("\nDo you want to play an other game ? y/n : ")
    if again != "y":
        print("\nThanks for playing !\n")
        break