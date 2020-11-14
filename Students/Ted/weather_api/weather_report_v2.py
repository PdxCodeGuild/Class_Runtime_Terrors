

import requests

class Mico:
    def __init__(self, name, location=[]):
        self.name = name
        self.location = location

    def city(self):
        city = 'government_camp'
        self.location.append(city)

    def latitude(self):
        lat = 45.297173
        self.location.append(lat)

    def longitude(self):
        lon = -121.807282
        self.location.append(lon)

    def current(self):
        current = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={self.location[0]}&lon={self.location[1]}&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')
        data = current.json()
        return data

    def direction(self):
        data = self.current()
        deg_num = data['wind']['deg']
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

while True:
    lat = float(input('what latitude? '))
    lon = float(input('what longitude? '))


    doit = Mico('texas',[lat, lon])
    #second = Mico('texas',[45.50848, -122.177388])
    data = doit.current()


    temp = data['main']['temp']
    speed = data['wind']['speed']


    print(f'Current temp near the hedgehogs is {temp}')
    print(f'The wind speed is {speed}mph, from the {doit.direction()}')

#loc_1 = Mico.location(Government_camp, 45.297173, -121.807282)
#larch_mt = 45.50848,-122.177388
#vernonia = 45.933846,-123.059346
#takhlakh = 46.277989,-121.596767
#current_2 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=45.297173&lon=-121.807282&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')

#current_2 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=45.50848&lon=-122.177388&units=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')



#future = requests.get('https://api.openweathermap.org/data/2.5/forecast/hourly?lat=45.297173&lon=-121.807282&=imperial&appid=8af2aa7fa978da0c3dc608a85406875c')

#past = requests.get('......')

#data_now_1 = current_1.json()
#data_now = current.json()
#data_future = future.json()  
#data_past = past.json()





#temp_now = data_now['main']['temp']
# feels = data['main']['feels_like']
# print(feels)
# print(f'Current temp near the hedgehogs is {temp_now}')
# print(f'The wind speed is {speed}mph, from the {direction()}')
#print(data)

# description_list = (data['weather'])
# description_dict = description_list[0]
# sky_description = description_dict['description']
# print(f'The sky description is "{sky_description}".')
