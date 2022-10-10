from internetspeedtwitterbot import InternetSpeedTwitterBot
import os
ACCOUNT = os.environ.get("account")
PASSWORD = os.environ.get("pass")
NAME = os.environ.get("name")
PROMISED_DOWN = 1000
PROMISED_UP = 600

complainer = InternetSpeedTwitterBot()
complainer.get_internet_speed()
down_speed = complainer.down
up_speed = complainer.up

if len(down_speed) < PROMISED_DOWN or len(up_speed) < PROMISED_UP:
    message = f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up" \
              f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

complainer.tweet_at_provider(ACCOUNT, NAME, PASSWORD, message)
