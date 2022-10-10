import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 51.507351
MY_LONG = -0.127758
my_email = "xxxxxxx@gmail.com"
password = "xxxxxxxxx"


# Todo: 1. If the ISS is close to my current position
# Your position is within +5 or -5 degrees of the ISS position.
def is_close_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    # print(iss_position)

    # Absolute value!
    long_minus = abs(MY_LONG - longitude)
    lat_minus = abs(MY_LAT - latitude)
    if long_minus <= 5 and lat_minus <= 5:
        return True
    else:
        return False


def is_dark(now):
    # API Parameters
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()
    sun_data = response2.json()
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    if (0 <= now < sunrise_hour) or (24 >= now > sunset_hour):
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject: Look Up👆\n\nThe ISS is above you in the sky")


while True:
    # Todo: BONUS: run the code every 60 seconds.
    time.sleep(10)
    if is_close_position():

        # Todo: 2.If it is currently dark
        now_hour = datetime.now().hour
        if is_dark(now=now_hour):
            # Todo: 3.Then email me to tell me to look up.
            send_email()
        else:
            print("Not Dark")
    else:
        print("Not position")


