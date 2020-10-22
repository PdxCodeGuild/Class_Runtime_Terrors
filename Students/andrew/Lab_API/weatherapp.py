import requests

city_pick = input("Please enter a city: N-New York| C-Chicago | P-Phoenix | L-Los Angeles: \n")
cityid = 0
city = ""
if city_pick == 'c':
    cityid = 3582383
    city = "Chicago"
if city_pick == 'n':
    cityid = 5128581
    city = "New York"
if city_pick == 'p':
    cityid = 5131135
    city = "Phoenix"
if city_pick == 'l':
    cityid = 5344994
    city = "Los Angeles"




response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={cityid}&appid=f4880b5dd2c51760b8ac4361e58abf6f')


weather = response.json()
conditions = weather['main']
print(weather)

if weather['cod'] != '404':
    temp = float(conditions['temp'])
    temp = (temp - 273.15) * 9/5 + 32
    print(f"The current temperature in {city} is... {temp} \n")
else:
    print("Sorry no weather data found.")





