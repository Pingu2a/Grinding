# NATO Alphabet Translator

This project is a CLI tool that converts any word or name into its corresponding NATO phonetic alphabet sequence (e.g., "Pingu" becomes ['Papa', 'India', 'November', 'Golf', 'Uniform']). It is a practical application of data manipulation to solve real-world spelling challenges.

This project teaches how to create dictionaries from CSV files using Pandas and how to use List Comprehensions to perform efficient data lookups.

**Sources that helped me:**

- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html
- https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- https://docs.python.org/3/library/os.path.html

## How to try

Just run the code in `/Grinding/PyLearning/Exercices/main.py` an type '18' for this game

## Logic
1. **Path Management**
   The program uses the `os` module to dynamically find the `letters.csv` file path. This ensures the script runs correctly regardless of which directory the terminal is currently in.
<br>
2. **Dictionary Comprehension with Pandas**
Instead of a simple list, the script converts the CSV data into a dictionary using `{row.letter: row.code for (index, row) in data.iterrows()}`. This creates a high-speed lookup table where every letter is a key linked to its phonetic code.
<br>

3. **User Input Normalization**
The input is automatically converted to uppercase using `.upper()`. This matches the keys in our dictionary, ensuring that whether the user types "hello" or "HELLO", the program finds the correct data.
<br>

4. **Data Transformation**
The core logic relies on a list comprehension: `[nato_dict[letter] for letter in usr_word]`.
    - It iterates through every character of the user's string.
    - It performs a key-value lookup in the NATO dictionary for each character.
    - It returns a neatly formatted list of strings.
<br>

5. **Loop and Utility Integration**
The game runs in a `while True` loop to allow multiple translations. It utilizes a custom utility function `y_or_n` to handle user confirmation, demonstrating clean code separation.