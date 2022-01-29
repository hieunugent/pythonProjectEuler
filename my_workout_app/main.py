import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID_TRACKER_API']
API_KEY = os.environ['API_KEY_TRACKER_API']
bearer_headers  ={
    "Authorization": f"Bearer {os.environ['ACCESS_TOKEN_SHEET_API']}",
}
GENDER ="male"
WEIGH_KG= 72.5
HEIGH_CM=174
AGE = 34
trackapi_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]
exercise_text = input("Tell me which exercise you did today: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg":WEIGH_KG,
    "height_cm":HEIGH_CM,
    "age":AGE
}

response = requests.post(url=trackapi_endpoint,
                         json=parameters, headers=headers)
result = response.json()
with open("my_workout_app/result.json", "w") as f:
    json.dump(result, f, indent=4)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
headers_1 = ("Authorization", "Basic aGVucnludWdlbnQ6YWJjMTIzNDU2ZGF5dG8=")
for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            
        }
    }

    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs,
        headers=bearer_headers
        )

