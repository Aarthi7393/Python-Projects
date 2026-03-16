import requests
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

proxy= os.getenv("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy

BASIC_AUTH = os.getenv("SHEETY_BASIC_AUTH")
BASIC_USERNAME = "pythontest"
BASIC_PASSWORD =  os.getenv("SHETTY_BASIC_PASS")
BEARER_AUTH = os.getenv("SHEETY_BEARER_AUTH")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/cac421c53c5c332e35b28886a7192d84/flightDeals/prices"
        self.basic_header = {
            "Authorization": f"Basic {BASIC_AUTH}",
        }
        self.bearer_header = {"Authorization": f"Bearer {BEARER_AUTH}"}



    def get_data(self):
        self.response = requests.get(self.sheety_url, headers=self.basic_header)
        print(self.response.json())
        self.data =self.response.json()["prices"]
        return self.data


    def update_iata_code(self):
        for city in self.data:
            put_param ={
            "price":{
                "iataCode":city["iataCode"],
                }
            }
            self.put_response = requests.put(f"{self.sheety_url}/{city['id']}" ,
                                             json=put_param, headers=self.basic_header)


# data_manager = DataManager()
# data_manager.get_data()