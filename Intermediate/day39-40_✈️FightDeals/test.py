import smtplib
my_email = "jennyroh96@gmail.com"
my_password = "hwdbghfndphdates"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="jing.lu.cn@outlook.com",
                        msg=f"Subject:test!\n\n£59".encode('utf-8'))
