from tkinter import *

def play_game():
    
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=300,height=200)
    window.config(padx=20,pady=20)
    
    def convert():
        global converted
        miles = float(miles_input.get())
        km = round(miles * 1.609,2)
        conv.config(text=f"{km}")

    miles_input = Entry(width=20)
    miles_input.grid(row=0,column=1)

    miles_txt = Label(text="Miles")
    miles_txt.grid(row=0, column=2)

    equal_txt = Label(text="is equal to")
    equal_txt.grid(row=1, column=0)

    conv = Label(text="0")
    conv.grid(row=1,column=1)

    kms_txt = Label(text="Km")
    kms_txt.grid(row=1, column=2)


    button = Button(text="Calculate", command=convert)
    button.grid(row=2,column=1)

    window.mainloop()