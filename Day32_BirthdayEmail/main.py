import random
import smtplib
import datetime as dt
import os
import pandas as pd

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("APP_PASSWORD")
#to_email = os.environ.get("TO_EMAIL")
PLACEHOLDER = "[NAME]"

data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
date = now.day
letters = ["letter_1", "letter_2", "letter_3"]


for key, value in data.iterrows():
    if value["month"] == month and value["day"] == date:
        name =value["name"]
        to_email = value["email"]
        letter = random.choice(letters)
        #letter_to_save = ""
        print(letter)
        with open (f"./letter_templates/{letter}.txt") as file:
            letter_to_save = file.read()
            letter_to_save= letter_to_save.replace(PLACEHOLDER, name)
            print(letter_to_save)
            # lines = file.readlines()
            # for line in lines:
            #     if PLACEHOLDER in line:
            #         line = line.replace(PLACEHOLDER, name)
            #     letter_to_save += line

        with  smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as connection:
            # with  smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as connection:
            # connection.starttls() #Encryption the email and secure the connection
            connection.login(user=my_email, password=password)  # Login
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter_to_save}".encode("utf-8")
                                )



