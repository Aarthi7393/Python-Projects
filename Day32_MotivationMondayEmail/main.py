import random
import smtplib
import datetime as dt
import os

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("APP_PASSWORD")
to_email = os.environ.get("TO_EMAIL")

with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = file.read().splitlines()
print(quotes)


current_quote = random.choice(quotes)
current_day = dt.datetime.now()
print(current_day)
if current_day.weekday() == 1:
    with  smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as connection:
    #with  smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as connection:
        #connection.starttls() #Encryption the email and secure the connection
        connection.login(user=my_email, password=password) # Login
        connection.sendmail(from_addr=my_email,
                            to_addrs= to_email,
                            msg= f"Subject:Happy Birthday!\n\n{current_quote}".encode("utf-8")
                            )