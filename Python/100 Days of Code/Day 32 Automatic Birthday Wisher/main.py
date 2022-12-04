import datetime as dt
import pandas
import random
import smtplib

# Getting the month and date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Reading the csv file using pandas
birthdays_dataframe = pandas.read_csv("birthdays.csv")

# Creating the dictionary for birtday_dataframe
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (
    index, data_row) in birthdays_dataframe.iterrows()}

# Checking the date
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_name = contents.replace("[NAME]", birthday_person["name"])

    my_email = "flacko.programming@gmail.com"
    password = "jksbgkstspntlvhi"

    # Sending the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")
