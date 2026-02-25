


# Password Manager

The Password Manager is a security tool designed to centralize and store login credentials locally. It provides a clean interface to generate strong, randomized passwords and save them into a structured JSON database, ensuring users never lose access to their accounts.

This project focuses on robust error handling, JSON data persistence, and advanced GUI layout management using Tkinter's grid system.


## Sources :

- https://pypi.org/project/pyperclip/
- https://www.w3schools.com/python/python_try_except.asp
- https://www.w3schools.com/python/python_json.asp

## How to try
Navigate to your project directory and run the `main.py` file.

The application allows you to:
- **Generate**: Create a randomized 12-18 character password (automatically copied to your clipboard).
- **Add**: Validate and save your credentials into a local database.
- **Search**: Instantly retrieve an email and password by typing the website name.

Click "**Add**" to save entries, and a confirmation popup will appear to ensure data accuracy.

## Logic

1.**JSON Data Persistence**

Unlike a standard text file, using a `.json` format allows for a "Key-Value" structure. This turns our database into a Python Dictionary where each **Website** is a unique key. This structure is essential for the search functionality, allowing the program to jump directly to the specific credentials without reading every line of the file.


>**Note**: We use `indent=4` in `json.dump` to keep the file human-readable.>

<br>

2.**Advanced Exception Handling** (`try/except/else`)

To prevent the app from crashing on its first run (when the file doesn't exist) or if the file is empty, we implemented a nested error handling logic. The code catches `FileNotFoundError` and `JSONDecodeError` to initialize a new dictionary, ensuring a seamless user experience regardless of the file's state.

<br>

3.**Password Generation & List Comprehension**

The generator uses **List Comprehensions** to gather randomized characters from three distinct groups (Letters, Numbers, and Symbols). By merging these lists and using `random.shuffle()`, we guarantee that the password doesn't follow a predictable pattern, significantly increasing security.

<br>

4.**Clipboard Automation** (`pyperclip`)

To enhance the workflow, the application integrates the `pyperclip` module. As soon as a password is generated and displayed in the UI, it is automatically copied to the system's clipboard. This eliminates the need for manual "Copy/Paste" actions, allowing the user to go directly to their browser and paste the new password immediately.

<br>

5.**The Search Mechanism**

By leveraging the Dictionary structure of JSON, the search function checks if the **website** string entered by the user exists as a key in our data. If found, it pulls the nested **email** and **password** values. This provides a "Query" logic similar to professional databases, providing instant feedback via a messagebox.

<br>

6.**Interface Alignment & Sticky Property**

To achieve a professional look with varying button sizes, we used the `sticky="ew"` property. This forces widgets to "stick" to the East and West edges of their grid cell, ensuring that the "Search" and "Generate" buttons align perfectly with the input fields.