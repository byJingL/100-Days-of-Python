import pandas
import datetime
import random
import smtplib

my_email = "xxxxxxx@gmail.com"
password = "xxxxxxxxx"

# ToDo: 1,Update the birthdays.csv
# new_birthdays = {
#     "name": ["Mom", "Dad", "brother"],
#     "email": ["mom@gmail.com", "dad@gmail.com", "lgy@gmail.com"],
#     "year": [1978, 1975, 2004],
#     "month": [8, 8, 8],
#     "day": [26, 26, 1],
# }
# file = pandas.DataFrame(new_birthdays)
# file.to_csv("birthdays.csv", index=False)

# ToDo: 2,Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
# 🧨important: make month and day to be a tuple
month = today.month
day = today.day

data = pandas.read_csv("birthdays.csv")
birth_today = []

for (index, row) in data.iterrows():
    if row["month"] == month and row["day"] == day:
        people = {
            row["name"]: row["email"],
        }
        birth_today.append(people)
print(birth_today)

# ToDo: 3,If step 2 is true, pick a random letter from letter templates
#  replace the [NAME] with the person's actual name from birthdays.csv

# ToDo: 4,Send the letter generated in step 3 to that person's email address.

for item in birth_today:
    for key in item:
        person_name = key
        person_email = item[key]
        print(person_email)
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as file:
            template = file.read()
        wisher = template.replace("[NAME]", person_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person_email,
                                msg=f"Subject: Happy Birthday!\n\n{wisher}")
