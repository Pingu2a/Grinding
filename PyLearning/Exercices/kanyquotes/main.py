from tkinter import *
import os
import requests

BASE_DIR = os.path.dirname(__file__)
background = os.path.join(BASE_DIR, "background.png")
kanye = os.path.join(BASE_DIR, "kanye.png")
def get_quote():
    iss = requests.get("https://api.kanye.rest")
    iss.raise_for_status()
    ip = iss.json()
    canvas.itemconfigure(quote_text,text=ip["quote"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=background)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 10, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()