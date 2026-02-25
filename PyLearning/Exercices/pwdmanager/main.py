from tkinter import *
from tkinter import messagebox
import os
import random
import pyperclip

BASE_DIR = os.path.dirname(__file__)
image = os.path.join(BASE_DIR, "logo.png")
datafile = os.path.join(BASE_DIR,"data.txt")

def play_pwdmanager():
    # Password Generator
    def pwdGen():

        LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMBERS = "0123456789"
        SYMBOLS = "!@#$%^&*"
        password = []

        pwd_letters = [random.choice(LETTERS) for _ in range(random.randint(8,10))]
        pwd_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2,4))]
        pwd_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2,4))]
        
        password = pwd_letters + pwd_numbers + pwd_symbols
        random.shuffle(password)
        final = "".join(password)

        pwd_input.delete(0,END)
        pwd_input.insert(0,final)
        pyperclip.copy(final)
    #Save datas into a txt file 
    def save():
        website = web_input.get()
        mail = mail_input.get()
        pwd = pwd_input.get()

        if len(website) == 0 or len(pwd) == 0:
            messagebox.showerror(title="Empty fields",message="Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail: {mail}\nPassword: {pwd}\nIs it ok to save ?")
            if is_ok:
                with open(datafile, "a") as data_file:
                    data_file.write(f"{website} | {mail} | {pwd}\n")
                
                web_input.delete(0,END)
                pwd_input.delete(0,END)

    window = Tk()
    window.title("Password manager")
    window.config(padx=20,pady=20)

    #image
    canvas = Canvas(width=200,height=200,highlightthickness=0)
    locker_img = PhotoImage(file=image)
    canvas.create_image(100,100,image=locker_img)
    canvas.image= locker_img
    canvas.grid(row=0,column=1)

    #Web Label
    web = Label(text="Website : ")
    web.grid(row=1,column=0)
    web_input = Entry(width=35)
    web_input.grid(row=1,column=1,columnspan=2,sticky="ew",pady=5)

    #Mail Label
    mail = Label(text="Email/Username : ")
    mail.grid(row=2,column=0)
    mail_input = Entry(width=35)
    mail_input.insert(0,"michel@email.com")
    mail_input.grid(row=2,column=1,columnspan=2,sticky="ew",pady=5)

    #Password Label
    pwd = Label(text="Password : ")
    pwd.grid(row=3,column=0)
    pwd_input = Entry(width=21)
    pwd_input.grid(row=3,column=1,sticky="ew",pady=5)

    #Password Button
    pwdGen = Button(text="Generate Password",command=pwdGen)
    pwdGen.grid(row=3,column=2,sticky="ew",pady=5,padx=5)

    #Adding Button
    adding = Button(text="Add", width=36,command=save)
    adding.grid(row=4, column=1,columnspan=2,sticky="ew",pady=5)


    window.mainloop()