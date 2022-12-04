import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_parameters = {
    "lat": 3.285680,
    "lon": 101.474030,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=weather_parameters)

weather_data = response.json()

hour = 0
will_rain = False

for time in weather_data["hourly"]:
    if weather_data["hourly"][hour]["weather"][0]["id"] < 700:
        will_rain = True
    hour += 1
    if hour == 13:
        break

if will_rain:
    print("Bring an umbrella")
