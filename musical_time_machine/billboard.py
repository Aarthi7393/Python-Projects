import requests
import html
from bs4 import BeautifulSoup
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
import os
# proxy = "http://internet.ford.com:83"
# os.environ ['http_proxy'] = proxy
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy


class BillBoard:
    def __init__(self, date):
        self.date = date

    def song_collection(self):
        response = requests.get(f"{BILLBOARD_URL}{self.date}/")
        response.raise_for_status()
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        top_list = soup.select("li ul li h3")
        song_list = [item.getText().strip() for item in top_list]
        return song_list
