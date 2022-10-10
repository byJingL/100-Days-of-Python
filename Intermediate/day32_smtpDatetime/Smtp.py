import smtplib

my_email = "xxxxxxx@gmail.com"
password = "xxxxxxxxx"

# Connect email sever
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # securing email connection
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="jing.lu.cn@outlook.com",
                        msg="Subject: Hello\n\nThis is the body of my email")
