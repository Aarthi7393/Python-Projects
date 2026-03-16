import requests
import os
import datetime

from requests.auth import HTTPBasicAuth

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy
API_ID = os.environ.get("NUTRI_API_ID")
API_KEY = os.environ.get("NUTRI_API_KEY")
BASE_URL = "https://app.100daysofpython.dev"
POST_URL =f"{BASE_URL}/v1/nutrition/natural/exercise"
GET_URL = f"{BASE_URL}/healthz"
SHEETY_URL = "https://api.sheety.co/cac421c53c5c332e35b28886a7192d84/workoutTracking/workouts"
BASIC_AUTH = os.environ.get("SHEETY_BASIC_AUTH")
BASIC_USERNAME ="pythontest"
BASIC_PASSWORD = os.environ.get("SHEETY_BASIC_PASSWORD")
BEARER_AUTH = os.environ.get("SHEETY_BEARER_AUTH")



nutri_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json',
}
nutri_parameter ={
    "query": input("Tell me which exercises you did:\n"
                   "Supported activities:\n"
                   "Running/Jogging - ran for 30 minutes, jogged 2 miles\n"
                    "Swimming - swam for 1 hour, swimming laps\n"
                    "Walking - walked 3 miles, brisk walk 45 min\n"
                    "Cycling - biked for 1 hour, rode bike 10 miles\n"
                    "Weightlifting - lifted weights 45 min, weight training: \n"),
    "weight_kg": 58,
    "height_cm": 165,
    "age": 33,
    "gender": "female"

}

responses = requests.post(POST_URL, headers=nutri_headers, json=nutri_parameter)
results = responses.json()["exercises"]
print(results)


for result in results:
    today=str(datetime.datetime.today().strftime("%d/%m/%Y"))
    time = str(datetime.datetime.today().strftime("%H:%M:%S"))
    exercise = result["name"]
    duration = result["duration_min"]
    calories = result["nf_calories"]

    sheety_parameter = {'workout':
                            {
                                'date': today,
                                'time': time,
                                'exercise': exercise,
                                'duration': duration,
                                'calories': calories
                            }
    }

    basic_header={
        "Authorization": f"Basic {BASIC_AUTH}",
    }

    bearer_header = {"Authorization": f"Bearer {BEARER_AUTH}"}

    #data_post = requests.post(SHEETY_URL, json=sheety_parameter, headers= bearer_header)
    data_post = requests.post(SHEETY_URL, json=sheety_parameter, headers=basic_header)
    print(data_post.status_code)
    print(data_post.json())

