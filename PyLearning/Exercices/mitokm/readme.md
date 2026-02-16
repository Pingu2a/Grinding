# Mile to Km Converter 

This project is a Graphical User Interface (GUI) application that performs real-time unit conversion. It provides a simple, user-friendly window where a user can input a distance in miles and instantly receive the equivalent distance in kilometers.
This project teaches how to build desktop applications using the Tkinter library, focusing on the Grid Geometry Manager and dynamic widget updates.

Sources that helped me:
- https://docs.python.org/3.14/library/tkinter.ttk.html#
- https://www.tcl-lang.org/man/tcl8.5/TkCmd/entry.htm

## How to try
You need to go inside /PyLearning/Exercices/ and run the main.py file and type '19'.

**Result**: A small window will appear. Enter a number in the input field and click "Calculate". The result will update dynamically on the screen.

## Logic

1. **Window Configuration**
   The program initializes a `Tk()` window with a specific minimum size and uses `.config(padx=20, pady=20)` to add internal padding. This ensures the widgets are not touching the edges of the window, creating a cleaner "Post-it" look.
   <br>
2. **The Grid System**
   Unlike previous projects using `.pack()`, this one uses `.grid()`. The interface is organized into a virtual table:
   - **Row 0:** Holds the entry field and the "Miles" label.
   - **Row 1**: Displays the static text "is equal to", the dynamic result, and the "Km" label.
   - **Row 2**: Contains the "Calculate" button, centered under the input.
  <br>
3. **Data Retrieval and Conversion**
   Inside the `convert()` function, the script uses the `.get()` method to pull the string from the Entry widget.
   - *Challenge*: Data from an Entry widget is always a string
   - *Solution*: We wrap it in `float()` to perform mathematical operations ($miles \times 1.609$).
  <br>
4. **Dynamic Widget Updating**
   Instead of re-creating a label every time, the script uses the .`config()` method: `conv.config(text=f"{km}")`. This tells Tkinter to keep the existing Label object but "refresh" the displayed text with the new calculation result.