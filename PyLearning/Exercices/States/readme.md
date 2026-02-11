# U.S. States Game

This project is an interactive educational game designed to test your knowledge of U.S. geography. Using a graphical interface, the script prompts the user to name all 50 states, placing the name of each correctly guessed state at its exact coordinates on the map.

This project teaches how to work with **CSV data** using the **Pandas** library and how to manage a coordinate-based graphical interface with **Turtle**.

Sources that helped me:

- https://pandas.pydata.org/docs/index.html
- https://docs.python.org/3/library/turtle.html


## How to try

You need to go inside the folder (`/PyLearning/Exercices`) and run the `main.py` file. **Result**: A window will open showing a blank map of the USA. Type names of states to fill the map. If you want to stop, type "**Exit**" to generate a list of the states you missed.

## Logic

1. **Screen and Image Setup** The program uses `turtle.addshape()` to load a .gif image of the U.S. map as the background. The window size is specifically set to `725x491` to match the image dimensions perfectly.
<br>
2. **Data Extraction with Pandas** The script reads `50_states.csv` and converts the "state" column into a Python list. This list is used to validate user input and track progress.
<br>
3. **Coordinate-Based Writing** When a correct state is entered, the program:
   - Filters the DataFrame to find the specific row for that state.
    - Extracts the `x` and `y` coordinates using the `.item()` method to convert Pandas data into a standard integer.
    - Moves a hidden "writer" turtle to those coordinates to print the state name on the map.
<br>
4. **Game State & Exit Logic** The game tracks the score and keeps a list of `guessed` states to prevent duplicates.
    - If the user types "**Exit**", the script uses a **list comprehension** to identify all states from the original list that are not in the `guessed` list.
    - These "missing states" are then exported into a new file called `states_to_learn.csv` for future study.