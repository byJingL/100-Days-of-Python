import requests
import os
import smtplib
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWT_API_KEY")
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
print(my_email)

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Using Slicing and For Loop
will_rain = False
weather_slice = weather_data["list"][:8]
for period in weather_slice:
    condition_code = period["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    massage = "It's gong to rain today. Remember to bring an ☔️"
else:
    massage = "It's not a rainy day! Have a good day!"

print("-----------------------------------------------")
# Just use For Loop
need_umbrella = False
for index in range(0, 8):
    weather_code = weather_data["list"][index]["weather"][0]["id"]
    if weather_code >= 700:
        print(weather_code)
    else:
        need_umbrella = True
        print("rain")
if need_umbrella:
    massage = "It's gong to rain today. Remember to bring an ☔️"
else:
    massage = "It's not a rainy day! Have a good day!"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject: Rain Alert\n\n{massage}")

