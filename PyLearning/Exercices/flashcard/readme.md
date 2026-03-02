# Flashcard App
Flashy is a language learning application designed to help users memorize vocabulary through a digital flashcard system. It uses an automated timer to reveal translations and tracks progress by removing known words from the study deck, ensuring a focused and efficient learning experience.

This project focuses on **dynamic UI updates, non-blocking asynchronous timers** with `.after()`, and **data persistence** using the Pandas library to manage CSV files.

<hr>

## Sources
- [Pandas Documentation - to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)
- [Tkinter Canvas Reference](https://www.tutorialspoint.com/python/tk_canvas.htm)
- [Python frequency words](https://github.com/hermitdave/FrequencyWords/tree/master/content/2018)

<hr>

## How to try
Navigate to your project directory and run the `main.py` file.

The application allows you to:

- **Learn**: View a French word and wait 3 seconds for the card to flip and reveal the English translation.
- **Skip**: Click the "**Wrong**" button to move to the next card without removing the current word from your list.
- **Master**: Click the "**Right**" button to mark a word as known. This saves your progress to a new file so you don't see that word again.

<hr>

## Logic
**1.File Path Synchronization**

The code starts by locating its own directory using `os.path.dirname(__file__)`. This is crucial for portability, especially when launched from a central menu. It builds absolute paths for images (cards and icons) and data files (original CSV and progress CSV).

**2.Data Initialization (Memory Management)**
<br>
The app manages word loading through a `try/except` block. It attempts to load `words_to_learn.csv` first. If it's the first time playing (File Not Found), it falls back to the original dataset. The data is converted into a list of **dictionaries** using `orient="records"` to allow easy random selection of "cards".

**3.The Next Card Logic (`next_card`)**
<br>

This is the core refresh function. Every time it's called, it **cancels** any existing `flip_timer` to prevent the card from flipping prematurely if the user clicks rapidly. It then picks a new random word, resets the Canvas to the front view (green background, black text), and schedules a new 3-second timer.

**4.The Flip Mechanism (`flip_card`)**
<br>

Triggered automatically after 3 seconds via `window.after()`, this function handles the visual transition. It swaps the background image to the **back view** and updates the text to show the English translation in white to maintain high contrast.

**5.Progress Persistence (`is_known`)**
<br>

When the user clicks the "Right" button, this function removes the current word from the active list in memory. It then immediately saves the updated list back to `words_to_learn.csv` using Pandas. This ensures that the word is permanently "learned" and won't appear in future sessions.


**6.UI Layering & Scope**
<br>

- **Canvas IDs**: By storing IDs like `card_bg` and `word_text`, the app uses `.itemconfig()` to update the UI instantly without redrawing the whole screen.
- **Nonlocal Keyword**: Since the functions are nested, `nonlocal` is used to allow the inner functions to modify variables like `current_card` and `flip_timer` defined in the parent scope.

**7.Interface Alignment**
<br>

The UI uses the Tkinter `grid` system. By utilizing `columnspan=2` for the main card and placing the buttons **side-by-side** in the following row, the layout remains balanced and professional.