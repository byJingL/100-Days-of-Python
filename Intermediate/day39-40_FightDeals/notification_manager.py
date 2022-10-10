import smtplib
from twilio.rest import Client
twilio_sid = "AC4c016cb3481e0c2d2cc35358abbaca1a"
twilio_token = "3cddaf458005760ea2752729633a69cf"
my_email = "jennyroh96@gmail.com"
my_password = "hwdbghfndphdates"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, text):
        client = Client(twilio_sid, twilio_token)
        message = client.messages.create(
            body=text,
            from_='+16184237591',
            to='+447784338893',
        )
        print(message.sid)

    def send_email(self, title, email_addr, main_body):
        text = f"Dear {title},\n\n{main_body}\n\nYours,\nJenny Flight Club"
        print(text)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_addr,
                                msg=f"Subject: Good Flight Deal!\n\n{text}".encode('utf-8'))
