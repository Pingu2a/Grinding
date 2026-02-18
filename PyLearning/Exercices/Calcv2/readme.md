# Calculator

I already did a calculator but this one is the volume 2 and the strongest !

A fully functional calculator with a sleek graphical user interface (GUI). This project explores user event handling and Python's ability to dynamically interpret complex mathematical expressions.

This project focuses on advanced Tkinter layout management, the power of the eval() function, and efficient code factorization using dictionary unpacking.

Sources :
 - https://realpython.com/python-eval-function/
 - https://www.w3schools.com/python/python_lambda.asp

## How to try

Navigate to /PyLearning/Exercices and run the main.py file.

The app allows you to:
- Perform basic arithmetic (+, -, x, /, %).
- **DEL**: Remove the last character if you made a mistake.
- **C**: Clear the entire screen for a new calculation.
- **=**: Execute the full string of operations at once.

## Logic

1. **The `eval()` Function**
Instead of coding complex logic for the order of operations (multiplication before addition), we use the native `eval()` function. It treats the string displayed on the screen as actual Python code and returns the result.
<br>
2. **The "String Slicing" Technique**
For the DEL button, we utilized Python's string slicing: text[:-1]. This command tells Python to keep everything from the start of the string up until the very last character, effectively "deleting" the end of the string without resetting the whole calculation.
<br>
3. **Keyword Argument Unpacking**`(**btn_params)`
To keep the code DRY (Don't Repeat Yourself), we stored the button styling (width, height, font) in a single dictionary. By using the `**` operator, we "unpack" these settings into every button. This makes the code much cleaner and allows for instant global design changes.
<br>
4. **UI Design & Alignment**
The interface uses a 5-column `grid` system. The display screen uses `columnspan=4` to stretch across the keypad, while the relief="sunken" attribute and `anchor="e"` (East) are used to mimic a real digital calculator screen where numbers are indented and aligned to the right.