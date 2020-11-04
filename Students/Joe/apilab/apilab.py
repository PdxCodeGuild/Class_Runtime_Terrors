import requests
city_name = input("city name: ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=london&&appid=8af2aa7fa978da0c3dc608a85406875c")
data = response.json()
visibility = data.get('visibility')
print (f' in {city_name}, visibility is {visibility} ft' )
weather = data.get('weather')
modified_weather = weather[0]['description']
print(f'Please expect {modified_weather}')
#for item in weather.key():
  #print (item)
'''for item in data.items():
    key = item[0]
    value = item[1]
    print (f'key : {key}')
    print(f'value: {value}')'''