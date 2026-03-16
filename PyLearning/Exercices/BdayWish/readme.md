# Birthday Wisher
The Birthday Wisher is an automation script designed to track birthdays from a database and send personalized celebratory emails. It checks the current date against a CSV file and, if a match is found, selects a random letter template, customizes it with the person's name, and dispatches it via SMTP.

This project focuses on **automated data filtering** with Pandas, **file system navigation**, and **secure email transmission** using Python’s standard libraries.

## Sources:
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [SMTPLIB](https://docs.python.org/3/library/smtplib.html)
- [OS module path manipulation](https://docs.python.org/3/library/os.path.html)


## How to try
Navigate to your project directory and run the `main.py` file. Ensure your birthdays.csv is populated and your `letter_templates/` folder contains at least one .txt file with the placeholder `[NAME].`

**Result**: The script will silently check the date. If a birthday matches today's date, the recipient will receive a personalized email automatically.

## Logic
**1. Robust Path Management**
The script uses `os.path.dirname(__file__)` combined with `os.path.join()` to define absolute paths for the CSV database and the templates folder. This ensures the script remains functional even when launched from an external directory or a central menu launcher.


**2. Advanced Data Filtering (Pandas)**
Instead of looping through the entire CSV manually, the script uses **Boolean Indexing**. By creating a `day_filter`, it compares the month and day columns against the current date simultaneously.

- **Result**: It creates a match **DataFrame** containing only the people celebrating their birthday today.

**3. Randomized Template Selection**
The `get_letter()` function utilizes `os.listdir()` to scan the templates folder and `random.choice()` to pick one file. This adds variety to the automation, ensuring that if multiple people have birthdays or if the script runs yearly, the letters aren't always identical.


**4. Dynamic String Manipulation**
Once a template is opened, the script uses the `.replace()` method. It searches for the specific placeholder `[NAME]` within the text and swaps it with the actual name retrieved from the CSV. This transforms a generic template into a personalized message.


**5. SMTP Protocol & Security**
The `send_mail()` function manages the connection to the Gmail **SMTP** server. It implements `connection.starttls()`, which encrypts the connection, ensuring that login credentials and email content are transmitted securely over the network.

**6. Iterating with `.iterrows()`**
To handle cases where multiple people share the same birthday, the script uses `.iterrows()`. This allows Python to loop through the filtered match **DataFrame** and extract the name and email for each person individually, triggering the mailing function for each one.