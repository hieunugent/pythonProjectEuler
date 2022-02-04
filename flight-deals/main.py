#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

# print(sheet_data)
ORIGIN_CITY_IATA ="LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    destinations = {
    data["iataCode"]:{ 
        "id":data["id"],
        "city":data["city"],
        "price":data["lowestPrice"]
        
        } for data in sheet_data}



today = datetime.now() +timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)  

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=today,
        to_time=six_month_from_today
    )
   
    
    if flight != None and flight.price < destinations[destination_code]["price"]:
       notification_manager.send_sms(
           message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} on {flight.leave_date} to {flight.return_date}",
       ) 
    
