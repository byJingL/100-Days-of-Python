import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TIME_SERIES = "TIME_SERIES_DAILY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://api.newscatcherapi.com/v2/search"
STOCK_KEY = "8CF9GWMGQNXJDDN7"
NEWS_KEY = "d_J6k69hG1jS-DDL-qyvV4iGw3p3FqN2tIAsvaU61Qw"
sid = "AC4c016cb3481e0c2d2cc35358abbaca1a"
token = "3cddaf458005760ea2752729633a69cf"


# Todo: 2,Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
def get_articles():
    parameters_news = {
        "q": COMPANY_NAME,
        "lang": "en",
        "search_in": "summary",
        "sort_by": "date",
    }
    headers = {"x-api-key": NEWS_KEY}
    response_news = requests.get(NEWS_ENDPOINT, headers=headers, params=parameters_news)
    response_news.raise_for_status()
    articles = response_news.json()
    first_3 = articles["articles"][:3]
    return first_3


# Todo: 3,Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
def send_message(data, articles):
    if data > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    formatted = [f"Headline: {article['title']}\nBrief: {article['excerpt']}" for article in articles]

    client = Client(sid, token)
    for item in formatted:
        formatted_message = f"{STOCK}: {up_down}{round(abs(data))}%\n{item}"
        print(formatted_message)
        message = client.messages.create(
            body=formatted_message,
            from_='+16184237591',
            to='+447784338893',
        )


# Todo: 1,Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": TIME_SERIES,
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}
response_stock = requests.get(STOCK_ENDPOINT, params=parameters)
response_stock.raise_for_status()
stock = response_stock.json()

# Solution 2
data = response_stock.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close_price = float(data_list[0]["4. close"])
before_yesterday_close_price = float(data_list[1]["4. close"])
print(yesterday_close_price, before_yesterday_close_price)

# Solution 1
yesterday = datetime.today().date() - timedelta(days=1)
before_yesterday = datetime.today().date() - timedelta(days=2)
yesterday_price = float(stock["Time Series (Daily)"][str(yesterday)]["4. close"])
before_yesterday_price = float(stock["Time Series (Daily)"][str(before_yesterday)]["4. close"])
print(yesterday_price, before_yesterday_price)

fluctuation = (yesterday_price - before_yesterday_price) / before_yesterday_price * 100
print(f"{abs(fluctuation)}%")

if abs(fluctuation) >= 0.5:
    three_articles = get_articles()
    send_message(fluctuation, three_articles)



