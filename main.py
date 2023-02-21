import requests
import os
# from dotenv import dotenv_values
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("PATH"))
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
api_key = os.getenv("api_key")
MY_PHONE = os.getenv("MY_PHONE")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
#response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=40.71&lon=-74.01&appid=1603e56e6f64ce1a78179485b7d4fd51")
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_= TWILIO_PHONE,
        to= MY_PHONE
    )

    print(message.status)

