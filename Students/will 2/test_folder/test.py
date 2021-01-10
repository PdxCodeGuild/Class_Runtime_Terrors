# 
import requests
# user input "city name"
city_name = input("Enter the city name of your intended destination: ")

# creates a variable that ".get" the data available for the associated city provided 
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&&appid=8af2aa7fa978da0c3dc608a85406875c")

# converts data to JAVA SCRIPT OBJECT NOTATION.json 
data = response.json()

# .gets the specific values for the specifc key within the dictionary
visibility = data.get('visibility')
weather = data.get('weather')

# .get the data at the 
modified_weather = weather[0]['description']

# print it!!!! provide the output for the user
print (f'''
Currently in {city_name.title()}, expect {modified_weather} with visibility at {visibility}''')
