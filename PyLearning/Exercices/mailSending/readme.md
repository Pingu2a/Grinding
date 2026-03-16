# Motivation Mailer
This project is an automated email notification system designed to send a burst of inspiration at the start of every week. It reads a collection of quotes from a local file, selects one at random, and dispatches it via email only if the current day is Monday.

This project focuses on **automated scheduling logic**, text file parsing, and implementing the **SMTP** protocol for network communication.

## Sources:
- [Python datetime module](https://docs.python.org/3/library/datetime.html)
- [SMTP server settings](https://mailmeteor.com/blog/gmail-smtp-settings)


## How to try
Ensure you have a `quotes.txt` file in the same directory as the script. Update the email credentials and the recipient address, then run the script.

**Result**: If today is Monday, the script will select a random quote and send it to the designated email address. If it is any other day, the script will execute without sending anything.

## Logic

**1. Environment-Aware File Access**

The script uses `os.path.dirname(__file__)` to establish a base directory. This prevents "File Not Found" **errors** when the script is called from a central launcher, ensuring the `quotes.txt` path is always relative to the script's actual location.


**2. File Ingestion and List Conversion**

By using the `.readlines()` method, the script reads the entire text file and converts every line into an individual string within a Python list. This structured format is essential for the subsequent **randomization** step.


**3. Randomized Selection**

The `random.choice()` function is applied to the list of quotes. This allows the script to pick exactly one motivational message per execution, ensuring the content remains fresh and unpredictable every week.


**4. Day-of-Week Validation**

Using `dt.datetime.now()` and `.weekday()`, the script identifies the current day as an **integer** (0 for Monday, 6 for Sunday). It then maps this to a custom days list to perform a string comparison.

- *Logic*: The expensive **SMTP** connection is only opened if the if condition confirms it is Monday.


**5. Secure SMTP Connection**

The script utilizes a with statement to manage the **SMTP** connection. This ensures the connection is automatically closed after the email is sent. The `connection.starttls()` command is used to upgrade an insecure connection to a secure one using **TLS (Transport Layer Security)**.


**6. Payload Construction**

The email is sent using an **f-string** that follows the standard email format: a "Subject" line, followed by two newlines (`\n\n`), and then the body (the quote). This structure is required for email clients to correctly distinguish between the header and the message content.