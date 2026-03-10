import requests
import os
from twilio.rest import Client


proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy

API_KEY =os.environ.get("TWILIO_API_KEY")
q="koeln,DE"
MY_LAT = 50.937531
MY_LONG =  6.960279
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
account_sid = os.environ.get("TWILIO_ACC_SID")
phone_no = "+15014346615"



# parameter = {
#     "q" : q,
#     "appid" :API_KEY,
# }
#
# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = parameter)
# response.raise_for_status()
OWM = "https://api.openweathermap.org/data/2.5/forecast"
parameter = {
    "appid" : API_KEY,
    "lat": -1.292066,
    "lon": 36.821945,
    "cnt" : 3
}
response = requests.get(OWM, params=parameter)
response.raise_for_status()
data = response.json()

weather_state = data["list"]
will_rain = False

for hour in weather_state:
    # code = data["list"][0]["weather"][0]["id"]
    code = hour["weather"][0]["id"]
    print(code)
    if int(code)<700:
        will_rain = True

if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It will rain today. Bring an umbrella!",
            from_=phone_no,
            to=os.environ.get("TO_PHONENUMBER")
        )

        print(message.sid)
        print(message.status)
