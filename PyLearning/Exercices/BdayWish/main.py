import smtplib
import datetime as dt
import os
import random
import pandas

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "birthdays.csv")
LETTER_FOLDER = os.path.join(BASE_DIR,"letter_templates")
birth_datas = pandas.read_csv(CSV_PATH)

today = dt.datetime.now()
month=today.month
day=today.day
day_filter = (birth_datas["month"] == month) & (birth_datas["day"] == day)
match = birth_datas[day_filter]

def get_letter(name):
    all_letters = os.listdir(LETTER_FOLDER)
    random_letter = random.choice(all_letters)
    file_path = os.path.join(LETTER_FOLDER,random_letter)
    with open(file_path) as ltr:
        content = ltr.read()
    new_ltr = content.replace("[NAME]",name)
    return new_ltr

def send_mail(mail,name):
    my_email = "mail.com"
    password = "pwd"
    letter_content = get_letter(name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Happy Birthday\n\n{letter_content}"
        )

for (index, row) in match.iterrows():
    send_mail(row["email"], row["name"])


