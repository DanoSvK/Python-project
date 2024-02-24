import pandas
import datetime as dt
import random
import smtplib


def handle_letters(name):
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = random.choice(letters)
    with open(f'letter_templates/{random_letter}') as file:
        letter = file.read()
    updated_letter = letter.replace('[NAME]', name)
    return updated_letter


def handle_sending(recipient, content):
    my_email = "YOUR_EMAIL_ADDRESS"
    password = "YOUR_EMAIL_APP_CODE"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject:Happy Birthday!\n\n{content}")


def handle_recipients():
    data = pandas.read_csv("birthdays.csv")
    people_dict = data.to_dict(orient="records")
    now = dt.datetime.now()
    for person in people_dict:
        if now.month == person["month"] and now.day == person["day"]:
            personalized_letter = handle_letters(person["name"])
            recipient = person["email"]
            handle_sending(recipient, personalized_letter)


handle_recipients()

