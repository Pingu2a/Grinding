user_score = 0
computer_score = 0
while True:
    import random

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    shapes = [
        r"""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """,
        r"""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """,
        r"""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
    ]

    # Function who gives the user win rate

    def WinRate(usr_score, cpt_score):
        total = usr_score + cpt_score

        if total > 0:
            win_rate = (usr_score / total) * 100
        else:
            win_rate = 0
        
        return win_rate
    # Function to check if user put wrong number or put char

    def choice_nbr(prompt, valid_choices):
        while True:
            answer = input(prompt)

            if answer.isdigit():
                value = int(answer)
            
                if value in valid_choices:
                    return value
            print("Invalid choice, try again : ")

    print("Welcome to the Rock, Paper, Cisors Game ! ")

    user_Choice = choice_nbr("What do you want to choose ? 0 for Rock, 1 for Paper, 2 for Cisors : ", [0, 1, 2])
    print(shapes[user_Choice])

    print("Computer choose :")
    computer_Choice = random.randint(0, 2)
    print(shapes[computer_Choice])

    if user_Choice == computer_Choice:
        print(YELLOW + "It's a draw" + RESET)
    elif (user_Choice == 0 and computer_Choice == 2) or (user_Choice == 1 and computer_Choice == 0)\
        or (user_Choice == 2 and computer_Choice == 1):
        print(GREEN + "You won !" + RESET)
        user_score += 1
    else:
        print(RED + "You lost :(" + RESET)
        computer_score += 1


    print(f"Your score : {user_score}\nComputer score : {computer_score}")
    print(f"Your win rate : {int(WinRate(user_score, computer_score))}%")
    again = input("Wanna play again ? (y/n) :")
    if again != "y":
        print("Thank you goodbye")
        print(f"Final score :\n You : {user_score} - {computer_score} : Computer ")
        print(f"Final Win rate : {int(WinRate(user_score, computer_score))}%")
        break