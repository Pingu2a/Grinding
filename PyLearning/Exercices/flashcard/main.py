from tkinter import *
import os
import pandas
import random


def play_flashcard():
    BACKGROUND_COLOR = "#B1DDC6"
    BASE_DIR = os.path.dirname(__file__)
    card_front = os.path.join(BASE_DIR,"images", "card_front.png")
    card_back = os.path.join(BASE_DIR, "images", "card_back.png")
    right_icon = os.path.join(BASE_DIR, "images", "right.png")
    wrong_icon = os.path.join(BASE_DIR, "images", "wrong.png")
    datas = os.path.join(BASE_DIR,"data", "french_words.csv")
    save_path = os.path.join(BASE_DIR, "data", "words_to_learn.csv")
    current_card = {}
    words_list = {}
    flip_timer = None

    try:
        data = pandas.read_csv(save_path)
    except FileNotFoundError:
        original_data = pandas.read_csv(datas)
        words_list = original_data.to_dict(orient="records")
    else:
        words_list = data.to_dict(orient="records")


    window = Tk()
    window.title("Flashy")
    window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)


    def next_card():
        nonlocal current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(words_list)
        front_card.itemconfig(title_text, text="French",fill="black")
        front_card.itemconfig(word_text, text=current_card["French"],fill="black")
        front_card.itemconfig(card_bg,image=front_img)
        flip_timer = window.after(3000,func=flip_card)


    def flip_card():
        front_card.itemconfig(title_text,text="English",fill="white")
        front_card.itemconfig(word_text,text=current_card["English"],fill="white")
        front_card.itemconfig(card_bg,image=back_img)

    def is_known():
        words_list.remove(current_card)
        dta = pandas.DataFrame(words_list)
        dta.to_csv(save_path,index=False)
        next_card()

    flip_timer = window.after(3000,func=flip_card)

    #flashcard
    front_card = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
    front_img = PhotoImage(file=card_front)
    back_img = PhotoImage(file=card_back)
    card_bg = front_card.create_image(400,263,image=front_img)
    front_card.image = front_img
    title_text = front_card.create_text(400, 150, text="French", font=("Ariel", 20, "italic"))
    word_text = front_card.create_text(400, 263, text="trouver", font=("Ariel", 30, "bold"))
    front_card.grid(row=0,column=0,columnspan=2)

    #Wrong button
    wrong_img = PhotoImage(file=wrong_icon)
    wrong_button = Button(image=wrong_img, highlightthickness=0,command=next_card)
    wrong_button.grid(row=1,column=0)

    #Right button
    right_img = PhotoImage(file=right_icon)
    right_button = Button(image=right_img, highlightthickness=0,command=is_known)
    right_button.grid(row=1,column=1)


    next_card()
    window.mainloop()