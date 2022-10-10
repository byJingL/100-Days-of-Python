import datetime as dt
import smtplib
import random

my_email = "xxxxxxx@gmail.com"
password = "xxxxxxxxx"
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 4:

    with open("quotes.txt") as file:
        # Pay attention to "readlines"
        quote_list = file.readlines()

    quote = random.choice(quote_list)
    print(quote)

    # Connect email sever
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # securing email connection
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="jing.lu.cn@outlook.com",
                            msg=f"Subject: Friday\n\n{quote}")
