from Quizz.question_model import Question
from .data import question_data
from .quiz_brain import QuizBrain
from utils.input_utils import y_or_n, clear

def test():
    is_on = True
    while is_on:
        i = 0
        question_bank = []
        for i in range(len(question_data)):
            test = Question(question_data[i]["text"], question_data[i]["answer"])
            question_bank.append(test)

        quiz = QuizBrain(question_bank)

        while quiz.still_has_question():
            quiz.next_question()

        print("You've completed the quizz")
        print(f"Your final score is : {quiz.usr_score}/{quiz.question_number}")

        play_again = y_or_n("\n Do you want to play again ? (y/n) :").lower()
        if play_again == 'y':
            clear()
        else:
            is_on = False