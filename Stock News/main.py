from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_daily_stock_difference():
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": "YOUR_API_KEY"
    }

    request = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
    data = request.json()

    yesterday_timestamp = dt.datetime.now().timestamp() - 86400
    two_days_ago_timestamp = dt.datetime.now().timestamp() - (86400 * 2)

    yesterday_date = dt.date.fromtimestamp(yesterday_timestamp)
    two_days_ago_date = dt.date.fromtimestamp(two_days_ago_timestamp)

    yesterday_stock_data = data["Time Series (Daily)"][f"{yesterday_date}"]["4. close"]
    two_days_ago_data = data["Time Series (Daily)"][f"{two_days_ago_date}"]["4. close"]

    percentage_difference = ((float(yesterday_stock_data) - float(two_days_ago_data)) / float(two_days_ago_data)) * 100

    if abs(percentage_difference) >= 5:
        get_news()


def get_news():
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": "YOUR_API_KEY"
    }

    request = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    data = request.json()
    articles = data["articles"][0:3]

    send_message(articles)


def send_message(articles):
    my_email = "YOUR_EMAIL_ADDRESS"
    password = "YOUR_EMAIL_APP_PASSWORD"

    for article in articles:
        subject = article["title"]
        content = article["description"]

        # Converting subject and content to utf-8 to avoid errors with unknown characters
        msg = MIMEMultipart()
        msg.attach(MIMEText(subject, 'plain', 'utf-8'))
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.as_string())


get_daily_stock_difference()
