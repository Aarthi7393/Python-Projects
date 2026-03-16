import requests
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
load_dotenv()

proxy= os.getenv("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
SERP_API_URL = "https://serpapi.com/search.json?"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iata_code(self,city_name):
        self.param = {
            "engine":"google_flights_autocomplete",
            "q": city_name,
            "api_key": os.getenv("SERPAPI_API_KEY"),
        }

        search = GoogleSearch(self.param)
        results = search.get_dict()
        try:
            suggestions = results["suggestions"][0]
            self.code = suggestions["airports"][0]["id"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            self.code = "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            self.code = "Not Found"
        return self.code

# flight_search = FlightSearch()