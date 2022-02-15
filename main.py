import requests
from twilio.rest import Client

twillio_password = "password"    # for twillio
phone_number = "+123456789"      # from twillio
API = "asdasdasdasdasdasd"          # for openweathermap
lat = 56.971986
lon = 24.165150
exclude = "minutely,current,daily"
account_sid = "asdasdadasdasd"      # for openweathermap
auth_token = "asdasdasdasdasd"      # for openweathermap

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}"
                            f"&appid={API}")
response.raise_for_status()
# data = response.json()['hourly']
# list_of_ids = [data[w_id]['weather'][0]['id'] for w_id in range(0, 12)]
#
# for i in list_of_ids:
#     if i < 700:
#         print("Bring an Umbrella")
#         break
# or can write like this
weather_slice = response.json()['hourly'][:12]
will_rain = False

for hours in weather_slice:
    condition_code = hours['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂.",
        from_=phone_number,
        to='+123456789'
    )
    print(message.status)
