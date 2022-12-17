import smtplib
import datetime as dt
import random


# Getting the current day of the week , 0 = Monday, 1 = Tuesday, 3 = ...
current_time = dt.datetime.now()
current_day_of_the_week = current_time.weekday()

# Creating a list from quotest.txt
with open("quotes.txt") as quotes_file:
    list_of_quotes = quotes_file.readlines()

# Sending the email
my_email = "flacko.programming@gmail.com"
password = "jksbgkstspntlvhi"
msg = random.choice(list_of_quotes)

if current_day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="flacko.programming@gmail.com",
                            msg=f"Subject: Monday Quotes\n\n{msg}")
