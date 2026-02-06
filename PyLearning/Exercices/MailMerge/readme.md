# Mail Merging Project

This project is an automated script to generate personalized invitation letters to my friends. It takes a template letter containing a placeholder and a list of names, then produces unique file for every person on the list.

This projet learns how to manipulate files in python (open, read, write).

Sources that helped me :

- https://www.w3schools.com/python/ref_string_replace.asp
- https://www.w3schools.com/python/ref_string_strip.asp
- https://www.w3schools.com/python/ref_file_readlines.asp

## How to try

You need to go inside MailMerge folder (/PyLearning/Exercices/MailMerge) and run the main.py file
Result : You'll see the created files inside the /Output/ReadyToSend folder.

## Logic

1. **Template reading**
   The program opens the `starting_letter.txt` file and stores the content as a string. This string contains a placeholder, `[names]`, which acts as a target for the replacement logic.
<br>
2. **Name List Processing**
   The script reads `invited_names.txt` using the `.readlines()` method.
   - Challenge : Each name in a text file usually ends with a hidden newline character (`\n`).
   - Solution : We use a loop or list comprehension with the `.strip()` method to "clean" the strings and remove any leading or trailing whitespace.
<br>
3. **String Substitution**
   Using the `.replace()` method, the script creates a new version of the letter for each name. It replaces the `[name]` placeholder with the cleaned name from our list.
<br>
4. **Automated file creation**
   For every person in the list, the script :
   - Generates a unique filename (e.g., `letter_for_Zuko.txt`).
   - Opens a new file in **Write Mode** (`"w"`) inside the `ReadyToSend` folder.
   - Writes the personalized content into that specific file.