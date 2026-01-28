import sys
from utils.input_utils import GREEN, RED,LIGHTPINK, RESET

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.usr_score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number} : {current_question.text} (true/false) : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, usr_answer, correct_answ):
        if usr_answer.lower() == 'q':
            sys.exit()
        if usr_answer.lower() == correct_answ.lower():
            print(f"\n{GREEN}You're right !{RESET}\n")
            self.usr_score += 1
        else:
            print(f"\n{RED}That's wrong !{RESET}\n")
        print(f"The correct answer was : {LIGHTPINK}{correct_answ}{RESET}.")
        print(f"Current score : {self.usr_score}/{self.question_number}\n")