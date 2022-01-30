from unittest import result
from urllib import response
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR_API_KEY_HERE"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]    
        code =results[0]["code"]
        return code
    def check_flights():
        pass
    