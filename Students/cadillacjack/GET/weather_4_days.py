import requests

zip = input("What is the zip code you would like to check? : ")


my_site = requests.get (f"http://pro.openweathermap.org/data/2.5/forecast/hourly?zip={zip},us&appid=3044c09eb7f6861149cd8417e5dcb030")
# 3044c09eb7f6861149cd8417e5dcb030
# my_site = requests.get (f"http://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid=f13b34adc98e544c0e9b823946d44c29")

data = my_site.json()

# city = data["name"]
# temp = data["main"]["temp"]
# wind_speed = data["wind"]["speed"]

# if data["wind"]["deg"] >= 0 < 45 or data["wind"]["deg"] >= 315 <= 360:
#     wind_dir = "North"
# elif data["wind"]["deg"] >= 45 < 135:
#     wind_dir = "East"
# elif data["wind"]["deg"] >=135 < 225:
#     wind_dir = "South"
# elif data["wind"]["deg"] >= 225 < 315:
#     wind_dir = "West"

# print(f'''
# In {city}, it is currently {temp} degrees.
# The wind currently blowing {wind_dir} at {wind_speed} MPH.
# ''')
print(data)