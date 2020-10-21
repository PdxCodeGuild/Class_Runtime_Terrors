import requests

zip = 97221
# zip = input('What is the Zip code of your weather request?\n')
current_wx_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip}&units=imperial&appid=api')

# forecast_wx_response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?zip={zip}&units=imperial&appid=api')


current_wx_data = current_wx_response.json()
# forecast_wx_data = forecast_wx_response.json()

temp = current_wx_data ["main"]["temp"]
feels_temp = current_wx_data ["main"]["feels_like"]
wind_speed = current_wx_data ["wind"]["speed"]
wind_direction = current_wx_data ["wind"]["deg"]
temp_max = current_wx_data ["main"]["temp_max"]
temp_min = current_wx_data ["main"]["temp_min"]
humidity = current_wx_data ["main"]["humidity"]

# print(f'The current weather data is {current_wx_data}\n\n')
# print(f'The foreceast weater data is {forecast_wx_data}\n\n')

sky_conditon_list = (current_wx_data ['weather'])
sky_condition_dictionary = sky_conditon_list[0]
sky_condition = sky_condition_dictionary["description"]

print (f'\nThe wind speed is {wind_speed} mph from {wind_direction} degrees.\n')
print(f'The current temperature is {temp} degrees F, which feels like {feels_temp} degrees F.\n')
print (f'The hmuidity is {humidity} percent.\n')
print(f'The maximum temperature is {temp_max} degrees F and the minimum temperature is {temp_min} degrees F.\n')
print (f'The sky condition is "{sky_condition}".')