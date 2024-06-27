import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 100


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,ta-IN;q=0.6,ta;q=0.5"
}

response = requests.get(URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "lxml")
price = soup.find(class_="aok-offscreen").getText().split("$")[1]
price_as_float = float(price)


if price_as_float<= TARGET_PRICE:
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_MAIL, password=MAIL_PASSWORD)
    connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject:AmazonPriceAlert"
                                                                       "\n\n Price has gone down and start buying")

    connection.close()