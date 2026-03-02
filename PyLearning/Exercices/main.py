import Calculator.ex as calc
import IMC.ex as imc
import TipCalc.ex as tip
import PizzaDelivery.ex as pizz
import TreasureIsland.ex as treasure
import RockPaperScisors.ex as rpc
import PWDGEN.ex as passwd
import Hangman.ex as hangman
import SecretAuction.ex as secret
import BlackJack.ex as Bj
import NumberGuessing.ex as nbGuess
import CoffeeMachine.ex as coffee
import Quizz.main as quizz
import Painting.ex as paint
import Snake.main as snake
import Pong.main as pong
import States.main as states
import nato.main as nato
import mitokm.ex as mito
import pomodoro.main as pomodoro
import Calcv2.main as calcv2
import pwdmanager.main as pwdmanager
import flashcard.main as flashcard
from utils.input_utils import clear, GREEN, RED, RESET

while True:
    print("Exercices :\n1: IMC\n2: Tip calculator\n3: Pizza Delivery\n4: Treasure Island\n5: Rock Paper Scisors\n6: Password Generator\
        \n7: Hangman\n8: Secret Auction\n9: Calculator\n10: BlackJack\n11: Number guessing\n" \
        "12: Coffe Machine\n13: Quizz\n14: Painting\n15: Snake Game\n16: Pong Game\n17: States Game\n"\
            "18: NATO Game\n19: Miles to Kms converter\n20: Pomodoro\n21: Calculator V2\n" \
                "22: Password manager\n23: Flascards\nq: quit")
    print("\nPS: For ex 14,15,16,17,18,19, 20, 21, 22, 23 you need to 'quit' the game before launching another one\n")
    
    choice = input("\nChoose an exercice : ")

    if choice == "1":
        print("""
    ========================================
            ⚖️  IMC CALCULATOR  ⚖️
    ========================================
    """)
        imc.imcCalc()
    elif choice == "2":
        print("""
    ========================================
            💸  TIP CALCULATOR
    ========================================
    """)
        tip.tipCalc()
    elif choice == "3":
        print("""
    ========================================
            🍕  PIZZA DELIVERY  🍕
    ========================================
    """)
        pizz.Pizza()
    elif choice == "4":
        print("""
    ========================================
            🏝️  TREASURE ISLAND  🏝️
    ========================================
    """)
        treasure.Treasure()
    elif choice == "5":
        print("""
    ========================================
        ✊ 🖐️ ✌️  ROCK PAPER SCISSORS
    ========================================
    """)
        rpc.RPS()
    elif choice == "6":
        print("""
    ========================================
            🔐  PASSWORD GENERATOR
    ========================================
    """)
        passwd.pwd()
    elif choice == "7":
        print("""
    ========================================
                🎯  HANGMAN
    ========================================
    """)
        hangman.Hang()
    elif choice == "8":
        print("""
    ========================================
            💰  SECRET AUCTION
    ========================================
    """)
        secret.SecretAuction()
    elif choice == "9":
        print("""
    ========================================
                🧮  CALCULATOR
    ========================================
    """)
        calc.calculator()
    elif choice == "10":
        print("""
    ========================================
                🃏  BLACKJACK
    ========================================
    """)
        Bj.BlackJack()
    elif choice == "11":
        print("""
    ========================================
                🔢 Number Guessing
    ========================================
    """)
        nbGuess.number_guessing()
    elif choice == "12":
        print("""
    ========================================
                🥛  Coffe Machine
    ========================================
    """)
        coffee.coffee_machine()
    elif choice == "13":
        print("""
    ========================================
                ❓  Quizz
    ========================================
    """)
        quizz.test()
    elif choice == "14":
        print("""
    ========================================
                🖼️  Painting
    ========================================
    """)
        paint.Hirst()
    elif choice == "15":
        print("""
    ========================================
                🐍  Snake Game
    ========================================
    """)
        snake.play_snake()
    elif choice == "16":
        print("""
    ========================================
                🏓  Pong Game
    ========================================
    """)
        pong.play_pong()
    elif choice == "17":
        print("""
    ========================================
                🇺🇸  States Game
    ========================================
    """)
        states.play_states_game()
    elif choice == "18":
        print("""
    ========================================
                🔤 NATO ALPHA
    ========================================
    """)
        nato.play_game()  
    elif choice == "19":
        print("""
    ========================================
                🚗 MILES TO KMS 
    ========================================
    """)
        mito.play_game() 
    elif choice == "20":
        print("""
    ========================================
                🍅 Pomodoro 
    ========================================
    """)
        pomodoro.play_pomodoro()
    elif choice == "21":
        print("""
    ========================================
                🧮 Calculator V2
    ========================================
    """)
        calcv2.play()    
    elif choice == "22":
        print("""
    ========================================
                🔐 Password manager
    ========================================
    """)
        pwdmanager.play_pwdmanager()
    elif choice == "23":
        print("""
========================================
            🎴  Flashcards 
========================================
""")
        flashcard.play_flashcard()
    elif choice == "q":
        print(GREEN + "\nThanks for playing !\n" + RESET)
        break
    else:
        print(RED + "invalid choice !\n" + RESET)
        continue
    clear()