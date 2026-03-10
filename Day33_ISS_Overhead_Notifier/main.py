import random
import smtplib
from datetime import datetime
import os
import requests
import time

MY_LAT = 50.937531
MY_LONG =  6.960279

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("APP_PASSWORD")
to_email = os.environ.get("TO_EMAIL")

def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hr = datetime.now().hour
    # if sunset <= current_hr <= sunrise:
    if current_hr >= sunset or current_hr <= sunrise:
        return True
    return None


def iss_overhead():
    response1 = requests.get(
        url="http://api.open-notify.org/iss-now.json",
       # timeout=10
    )
    response1.raise_for_status()
    data1 = response1.json()
    iss_longitude = float(data1["iss_position"]["longitude"])
    iss_latitude = float(data1["iss_position"]["latitude"])
    if MY_LAT+5 <= iss_latitude <= MY_LAT+5 and MY_LONG+5 <= iss_longitude <= MY_LONG+5:
        return True
    return None






while True:
    if is_night() and iss_overhead():
        print("True")
        with  smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as connection:
            # with  smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as connection:
            # connection.starttls() #Encryption the email and secure the connection
            connection.login(user=my_email, password=password)  # Login
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:ISS Locator Alert!\n\n Look up!!!!"
                                )
    else:
        print("False")
    time.sleep(60)