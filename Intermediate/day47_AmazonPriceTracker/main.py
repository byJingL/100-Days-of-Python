import requests
from bs4 import BeautifulSoup
import os
import smtplib

URL = "https://www.amazon.co.uk/Philips-DiamondClean-Toothbrush-Intensities-Connected/dp/B087VLVSLD" \
      "/ref=sr_1_7?crid=1IAYEI5YHDTZF&keywords=phillips%2Bsonicare%2Belectric%" \
      "2Btoothbrush&qid=1664043210&sprefix=pelectric%2Btoothbrush%2Caps%2C69&sr=8-7&th=1"
TARGET_PRICE = 165
MY_EMAIL = os.environ.get("email")
MY_PASSWORD = os.environ.get("password")


def send_email(body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Amazon Price Alert!\n\n{body}")
    print("Email Sent!")


# Todo 1. Use BeautifulSoup to Scrape the Product Price
headers = {
    "Accept-Language": "XXXXXXX",
    "User-Agent": "XXXXXXXXX",
}
response = requests.get(URL, headers=headers)
response.raise_for_status()
# with open("web.txt", "w") as file:
#     file.write(response.text)
# with open("web.txt") as file:
#     web_page = file.read()

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
title = soup.find(name="span", id="productTitle").getText()
price = soup.find(name="span", class_="a-offscreen").getText()
# format information
product_title = title.split(",")[0].strip()
current_price = float(price.split("£")[1])

# Todo 2. Email Alert When Price Below Preset Value
if current_price <= TARGET_PRICE:
    message = f"{product_title} is now {current_price} GBP!\n\nPlease check: {URL}"
    send_email(body=message)
