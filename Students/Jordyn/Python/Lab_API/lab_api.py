import requests

def wind_cardinal(degree):
    if degree in range(-1, 24) or degree in range(337, 361):
        return 'North'
    elif degree in range(23, 68):
        return 'North East'
    elif degree in range(67, 114):
        return 'East'
    elif degree in range(113, 158):
        return 'South East'
    elif degree in range(157, 204):
        return 'South'
    elif degree in range(203, 248):
        return 'South West'
    elif degree in range(247, 294):
        return 'West'
    elif degree in range(293, 338):
        return 'North West'

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8af2aa7fa978da0c3dc608a85406875c&units=standard'.format(city)

weather = requests.get(url)

data = weather.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
wind_direction = data['wind']['deg']
direction_card = wind_cardinal(wind_direction)
description = data['weather'][0]['description']

print('Temperature : {} F'.format(temp))
print('Wind Speed : {} mph'.format(wind_speed))
print('Wind Direction : {}°: {}'.format(wind_direction, direction_card))
print(description.title())