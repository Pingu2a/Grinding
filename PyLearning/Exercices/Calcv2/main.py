from tkinter import *

def play():
    window = Tk()
    window.title("Calculator")
    window.config(padx=30, pady=30)

    def pressed(val):
        txt = screen_calc.cget("text")
        if val == "=":
            try:
                result = eval(txt)
                screen_calc.config(text=str(result))
            except:
                screen_calc.config(text="ERROR")
        elif val == "C":
            screen_calc.config(text="")
        elif val == "DEL":
            new_txt = txt[:-1]
            screen_calc.config(text=new_txt)
        else:
            
            screen_calc.config(text=txt + val)

    screen_calc = Label(
        text="", 
        bg="#f0f0f0", 
        font=("Courier", 18),
        relief="sunken", 
        bd=3,
        width=15,
        anchor="e", 
        padx=2
    )
    screen_calc.grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky="ew")

    btn_params = {"width": 5, "height": 2, "font": ("Arial", 12)}


    # Line 1
    Button(text="7", command=lambda: pressed("7"), **btn_params).grid(row=1, column=0)
    Button(text="8", command=lambda: pressed("8"), **btn_params).grid(row=1, column=1)
    Button(text="9", command=lambda: pressed("9"), **btn_params).grid(row=1, column=2)
    Button(text="%", command=lambda: pressed("%"), **btn_params).grid(row=1, column=3)
    Button(text="C", command=lambda: pressed("C"), **btn_params).grid(row=1, column=4)

    # Line 2
    Button(text="4", command=lambda: pressed("4"), **btn_params).grid(row=2, column=0)
    Button(text="5", command=lambda: pressed("5"), **btn_params).grid(row=2, column=1)
    Button(text="6", command=lambda: pressed("6"), **btn_params).grid(row=2, column=2)
    Button(text="/", command=lambda: pressed("/"), **btn_params).grid(row=2, column=3)
    Button(text=".", command=lambda: pressed("."), **btn_params).grid(row=2, column=4)

    # Line 3
    Button(text="1", command=lambda: pressed("1"), **btn_params).grid(row=3, column=0)
    Button(text="2", command=lambda: pressed("2"), **btn_params).grid(row=3, column=1)
    Button(text="3", command=lambda: pressed("3"), **btn_params).grid(row=3, column=2)
    Button(text="x", command=lambda: pressed("*"), **btn_params).grid(row=3, column=3)
    Button(text="DEL", command=lambda: pressed("DEL"), **btn_params).grid(row=3, column=4)

    # Line 4
    Button(text="0", command=lambda: pressed("0"), **btn_params).grid(row=4, column=0)
    Button(text="=", command=lambda: pressed("="), **btn_params).grid(row=4, column=1)
    Button(text="+", command=lambda: pressed("+"), **btn_params).grid(row=4, column=2)
    Button(text="-", command=lambda: pressed("-"), **btn_params).grid(row=4, column=3)
    Button(text="(", command=lambda: pressed("("), **btn_params).grid(row=4, column=4)
    Button(text=")", command=lambda: pressed(")"), **btn_params).grid(row=5, column=4)

    window.mainloop()