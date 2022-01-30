#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
ORIGIN_CITY_IATA ="LAX"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()   

tommorrow = datetime.now() +timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)  

for  destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tommorrow,
        to_time=six_month_from_today
    )
  