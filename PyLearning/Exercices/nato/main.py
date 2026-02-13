import pandas
from utils.input_utils import y_or_n
import os 


def play_game():
    BASE_DIR = os.path.dirname(__file__)
    csv_path = os.path.join(BASE_DIR, "letters.csv")
    data = pandas.read_csv(csv_path)

    nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    while True:
        usr_word = input("Enter a word : ").upper()
        to_nato = [nato_dict[letter] for letter in usr_word]
        print(to_nato)
        again = y_or_n("Wanna play again ? (y/n) :")
        if again == 'n':
            return