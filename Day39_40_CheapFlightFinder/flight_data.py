import os
import requests
import serpapi
from serpapi import GoogleSearch
import datetime
from dotenv import load_dotenv
load_dotenv()

proxy= os.getenv("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
SEARCH_URL = "https://serpapi.com/search.json"

today = datetime.date.today()
from_time = today + datetime.timedelta(days=1)
to_time = today + datetime.timedelta(days=20)


DEPARTURE = "DUS"
currency = "EUR"


fly_type = "1"
'''1 - Round trip (default)
2 - One way
3 - Multi-city'''

# onward_journey = str(from_time.strftime("%Y-%m-%d"))
# return_journey = str(to_time.strftime("%Y-%m-%d"))

onward_journey = "2026-04-30"
return_journey = "2026-05-16"

max_price = "1500"

engine = "google_flights"
api_key = os.getenv("SERPAPI_API_KEY")

bags = "2"
adults = "2"

#https://serpapi.com/search.json?engine=google_flights&departure_id=PEK&arrival_id=AUS&outbound_date=2026-03-11&return_date=2026-03-17&currency=USD&hl=en

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.stops = 1

    def find_flights(self,data):
            #print(data["iataCode"])
        google_flights_endpoint = "https://serpapi.com/search"
        flights_parameters = {
            "engine": "google_flights",
            "departure_id": DEPARTURE,
            "arrival_id": data["iataCode"],
            "outbound_date": onward_journey,
            "return_date": return_journey,
            "currency": "EUR",
            "api_key": api_key,
            "max_price": max_price,
            "deep_search" : "True",
            "stops" : self.stops
        }

        response = requests.get(url=google_flights_endpoint, params=flights_parameters)
        # print(response.status_code)
        #print(response.json())
        try:
            lowest_price = response.json()["price_insights"]["lowest_price"]
            #print(f"Lowest_price: {lowest_price}")
        except KeyError:
            try:
                lowest_price = response.json()["best_flights"][0]["price"]
            except (KeyError, IndexError):
                lowest_price = "N/A"
        # return lowest_price
        return lowest_price, onward_journey, return_journey


# flight_data = FlightData()
# price = flight_data.find_flights()
# if price == "N/A":
#     flight_data.stops = 0
#     price = flight_data.find_flights()
#
# print(f"Getting flights for BLR.... € {price} ")
# flight_data = FlightData()
# print(flight_data.stops)