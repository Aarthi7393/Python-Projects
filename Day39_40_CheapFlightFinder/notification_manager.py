import smtplib
import os
import requests
from dotenv import load_dotenv
load_dotenv()

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
my_email = os.environ.get("MY_EMAIL")
to_email = os.environ.get("TO_EMAIL")
password = os.environ.get("APP_PASSWORD")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        self.message = message
        BASIC_AUTH = os.getenv("SHEETY_BASIC_AUTH")
        BASIC_USERNAME = "pythontest"
        BASIC_PASSWORD = os.getenv("SHETTY_BASIC_PASS")
        BEARER_AUTH = os.getenv("SHEETY_BEARER_AUTH")
        self.sheety_url = "https://api.sheety.co/cac421c53c5c332e35b28886a7192d84/flightDeals/users"
        self.basic_header = {
            "Authorization": f"Basic {BASIC_AUTH}",
        }
        self.bearer_header = {"Authorization": f"Bearer {BEARER_AUTH}"}
        self.response = requests.get(self.sheety_url, headers=self.basic_header)
        self.send_message()

    def send_message(self):
        print(self.response.text)
        for user in self.response.json()["users"]:
            print(user["whatIsYourEmail?"])
        # with  smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as connection:
        #     # with  smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as connection:
        #     # connection.starttls() #Encryption the email and secure the connection
        #     connection.login(user=my_email, password=password)  # Login
        #     connection.sendmail(from_addr=my_email,
        #                         to_addrs=to_email,
        #                         msg=f"Subject:Low Flight Price Alert!{self.message}"
        #                         )