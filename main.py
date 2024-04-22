import requests
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "c41b6ee2108bb27a549c00e58ad7aa5c"
parameter = {
    "lat": 9.005401,
    "lon":  38.763611,
    "appid": api_key,
}
response = requests.get(url=OWM_ENDPOINT, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_splice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_splice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code > 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")
