# import smtplib
# import datetime as dt
# import os
# import random



# BASE_DIR = os.path.dirname(__file__)
# txt_path = os.path.join(BASE_DIR, "quotes.txt")
# with open(txt_path) as quotes:
#     content = quotes.readlines()

# motivation_msg = random.choice(content)

# days = ["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# now = dt.datetime.now()
# day_of_week = days[now.weekday()]

# if day_of_week == "monday":
#     my_email = "my_mail@..."
#     password = "passwd..."

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="mail@mail",
#             msg=f"Subject:Motivation\n\n{motivation_msg}"
#         )