import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


def send_email(price_float):
    my_email = "YOUR_EMAIL_ADDRESS"
    password = "YOUR_APP_PASSWORD"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='d.kopac@gmail.com', msg=f"Subject:Price changed!\n\nA price has dropped! The current price is ${price_float}.")


def get_price():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language":"en-GB,en;q=0.9,sk;q=0.8,sk-SK;q=0.7,cs;q=0.6,en-US;q=0.5"
    }
    res = requests.get(url='https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1', headers=header)

    soup = BeautifulSoup(res.content, "lxml")
    price = soup.find(name='span', class_="aok-offscreen").getText()
    price_float = float(price.split('$')[1])
    if price_float < 100:
        send_email(price_float)


get_price()