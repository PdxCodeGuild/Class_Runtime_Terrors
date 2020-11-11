

import requests
#zip = 97202
#zip = input('What is the Zip code of your weather request?\n')
#hedghog = 45.297173,-121.807282
#larch_mt = 45.50848,-122.177388
#vernonia = 45.933846,-123.059346
#takhlakh = 46.277989,-121.596767
current_2 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=45.297173&lon=-121.807282&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')

#current_2 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=45.50848&lon=-122.177388&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')



#future = requests.get('https://api.openweathermap.org/data/2.5/forecast/hourly?lat=45.297173&lon=-121.807282&=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')

#past = requests.get('......')

#data_now_1 = current_1.json()
data_now_2 = current_2.json()
#data_future = future.json()  
#data_past = past.json()



speed = data_now_2['wind']['speed']
#deg_num = data['wind']['deg']

def direction():

  deg_num = data_now_2['wind']['deg']
  if deg_num >= 22.5 and deg_num < 67.5:
    return('NorthEast')
  elif deg_num >= 67.5 and deg_num < 112.5:
    return('East')
  elif deg_num >= 112.5 and deg_num < 157.5:
    return('SouthEast')
  elif deg_num >= 157.5 and deg_num < 202.5:
    return('South')
  elif deg_num >= 202.5 and deg_num < 247.5:
    return('SouthWest')
  elif deg_num >= 247.5 and deg_num < 292.5:
    return('West')
  elif deg_num >= 292.5 and deg_num < 337.5:
    return('NorthWest')
  elif deg_num >= 337.5 or deg_num < 22.5:
    return('North')

temp_now = data_now_2['main']['temp']
# feels = data['main']['feels_like']
# print(feels)
print(f'Current temp near the hedgehogs is {temp_now}')
print(f'The wind speed is {speed}mph, from the {direction()}')
#print(data)

# description_list = (data['weather'])
# description_dict = description_list[0]
# sky_description = description_dict['description']
# print(f'The sky description is "{sky_description}".')
