import requests
from datetime import datetime

EXERCISE = "Ran 2 miles and walked for 3 miles"
GENDER = "female"
WEIGHT = 48
HEIGHT = 160
AGE = 26
APPLICATION_ID = "3e5d9733"
APPLICATION_KEY = "023b6d042494d656c4a012a455aec80b"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
    "Content-Type": "application/json"
}
info = input("Tell me which exercises you did: ").lower()
params = {
    "query": info,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, headers=headers, json=params)
result = response.json()["exercises"]

sheet_endpoint = "https://api.sheety.co/d65ba2aab1558fc6f0e2790b0514e29f/myWorkouts/sheet1"
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
print(today, time)
headers = {
    "Authorization": "Basic amVubnlyb2g6amdkYWxrZmpoa2Zu"
}
for item in result:
    # Parameters have to be lower case
    body = {
        "sheet1": {
            "date": today,
            "time": time,
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories']
        }
    }
    input_response = requests.post(url=sheet_endpoint, json=body, headers=headers)
    print(input_response.text)
