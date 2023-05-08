import requests
from twilio.rest import Client

# type account id here
account_sid = ''

# type token in here
auth_token = ''

# type personal api key here
api_key = ""

# type custom latitude and longitude for location
LAT = 0
LONG = 0

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
request.raise_for_status()
weather_data = request.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to rain today. Dress up properly ☔☔🌧🌧",
        from_='+13236498424',

        # type personal number here
        to=''
    )
