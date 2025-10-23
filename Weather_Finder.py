import requests

city = input("Which city do you want to know the weather about? ")

# Step 1: Get lat/lon from Geo API
geo_url = "http://api.openweathermap.org/geo/1.0/direct"
second= requests.get(geo_url)
print(second.json())
geo_params = {
    "q": city,
    "limit": 1,
    "appid": "78c78c2fefab26474bb970569894ece3"
}
geo_response = requests.get(geo_url, params=geo_params)
res = geo_response.json()[0]
lat, lon = res["lat"], res["lon"]

# Step 2: Get weather info
weather_url = "https://api.openweathermap.org/data/2.5/weather"
print
# dataa={
#     "mullah":"tulla",
# }
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": "78c78c2fefab26474bb970569894ece3",
    "units": "metric"
}

weather_response = requests.get(weather_url, params=weather_params)
# weather=requests.post(weather_url, params=dataa)
# weather_response=requests.put(weather_url, params=dataa)
weather_data = weather_response.json()
print(weather_data.__dir__())

# Extract info
temp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]
# in this i am telling the weather dict to go inside yourself and bring me the value of the key description inside you
# humidity1 = weather_data["dataa"]["mullah"]
condition = weather_data["weather"]

# Step 3: Let user choose
player_choice = input("What do you want to know? (lat, lon, temp, humidity, condition): ").lower()

if "lat" in player_choice:
    print(f"Latitude: {lat}, Longitude: {lon}")

elif "temp" in player_choice:
    print(f"Temperature: {temp}°C")

elif "humidity" in player_choice:
    print(f"Humidity: {humidity}%")

elif "condition" in player_choice:
    print(f"Condition: {condition}")

else:
    print("❌ Invalid choice! Please choose from: lat, lon, temp, humidity, condition")
