import requests
def wind_cardinal(degree):
    if degree in range(-1, 46) or degree in range(315, 361):
        return 'N'
    elif degree in range(45, 136):
        return 'E'
    elif degree in range(135, 226):
        return 'S'
    elif degree in range(225, 316):
        return 'W'
city = input('Enter your city : ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8af2aa7fa978da0c3dc608a85406875c&units=imperial'.format(city)
weather = requests.get(url)
data = weather.json()
temp = data['main']['temp']
wind_speed = data['wind']['speed']
wind_direction = data['wind']['deg']
direction_card = wind_cardinal(wind_direction)
description = data['weather'][0]['description']
print('Temperature : {} F'.format(temp))
print('Wind Speed : {} mph'.format(wind_speed))
print('Wind Direction : {}: {}'.format(wind_direction, direction_card))
print(description.title())