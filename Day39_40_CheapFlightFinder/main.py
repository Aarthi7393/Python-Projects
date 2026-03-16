#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data =data_manager.get_data()

# ==================== Update the Airport Codes in Google Sheet ====================
flight_search = FlightSearch()
for data in sheet_data:
    # if data['iataCode'] == "":
        data['iataCode'] = flight_search.get_iata_code(data["city"])

data_manager.data =sheet_data
data_manager.update_iata_code()

# ==================== Search for Flights ====================
flight_data = FlightData()
for data in sheet_data:
    message = ""
    flight_data.stops = 1
    price_date_details = flight_data.find_flights(data)

    if price_date_details[0] == "N/A":
        flight_data.stops = 0
        price_date_details = flight_data.find_flights(data)
    print(f"Getting flights for {data["city"]}..... ")
    print(f"{data["city"]} :  € {price_date_details[0]}")


    try:
        if price_date_details[0] < data["lowestPrice"]:
            message += (f"Low price Alert! Only € {price_date_details[0]} to fly from DUS to {data["city"]}"
                f" on {price_date_details[1]}  until {price_date_details[2]}")
            notification_manager = NotificationManager(message)
    except TypeError:
        message = ""
    if message != "":
        print(message)