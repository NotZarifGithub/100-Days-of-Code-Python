import requests
from datetime import datetime
import datetime as dt
import smtplib
import time

MY_LAT = 3.285680
MY_LNG = 101.474030
my_email = "flacko.programming@gmail.com"
password = "jksbgkstspntlvhi"


def is_night():

    MYUTC = datetime.utcnow().hour - datetime.now().hour

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Convert to datetime
    sunrise = datetime.strptime(
        data["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
    sunset = datetime.strptime(
        data["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z")

    # Substact hours from response and sunset
    sunrise -= dt.timedelta(hours=MYUTC)
    sunset -= dt.timedelta(hours=MYUTC)

    time = dt.datetime.now().hour

    if time >= sunset or time <= sunrise:
        return True


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    iss_position = (iss_longitude, iss_latitude)

    if MY_LAT-5 <= iss_latitude <= MY_LNG+5:
        if MY_LNG-5 <= iss_longitude <= MY_LNG+5:
            return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject: Look Up!!\n\nThe International Space Station is currently on top of your head!")

