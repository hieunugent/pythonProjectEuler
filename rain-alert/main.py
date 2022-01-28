
from http import client
import requests
import json
import os 
from twilio.rest import Client

apikey = os.environ['APIKEY']
account_sid = os.environ['ACCOUNT_SID']
auth_token= os.environ['AUTH_TOKEN']
parameter={
    "lat": "37.8267",
    "lon": "-122.4233",   
    "appid": apikey,
}

will_rain = False
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It will rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain",
        from_="+12058360025",
        to="+917007870983"
    )
 




# with open("rain-alert/rain-alert.json", "r") as data_file:
#     weather_data = json.load(data_file)
#     # print(old_data["hourly"][0]["weather"][0]["id"])
#     weather_slice = weather_data["hourly"][0:10]   
#     for hour_data in weather_slice:
#         condition_code = hour_data["weather"][0]["id"]
#         if int(condition_code) < 700:
#             will_rain = True
# if will_rain: 
#     print("It will rain")
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="It will rain",
#         from_="+12058360025",
#         to="+917007870983"
#     )
    
# else:
#     print("It will not rain")
