import smtplib

my_email = "flacko.programming@gmail.com"
password = "jksbgkstspntlvhi"
msg = "sup bitch"

connection = smtplib.SMTP("smtp.gmail.com", 587)

# Securing the process
connection.starttls()

# Logging in the gmail account
connection.login(user=my_email, password=password)

# Sending the email
connection.sendmail(from_addr=my_email,
                    to_addrs="ronaldo7zarif@gmail.com", msg=f"Subject: TESTING\n\nsup bitchesss")

# Closing the process
connection.close()

## or ##

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="flacko.programming@gmail.com",
                        msg=f"Subject: Monday Quotes\n\n{msg}")
