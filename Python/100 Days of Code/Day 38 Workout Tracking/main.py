import requests
from datetime import datetime


APP_ID = "975e012d"
API_KEY = "7218a013cd52ea2ebf3ae7fa5be9f19c"

nutrionix_end = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_end = "https://api.sheety.co/b0e8664bcf50ee02e1a5dac12a79f3ab/workoutTracker/workouts"

GENDER = "male"
WEIGHT_KG = 81
HEIGHT_CM = 175
AGE = 21

nutrionix_json = {
    "query": input("Tell me which exercises you did: ")
}

nutrionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(
    url=nutrionix_end, headers=nutrionix_header, json=nutrionix_json)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_json = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_bearer = {
    "Authorization": "Bearer azazazazazazaz7"
}

response = requests.post(
    url=sheety_end, json=sheety_json, headers=sheety_bearer)
