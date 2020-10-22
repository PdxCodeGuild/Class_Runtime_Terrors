import requests

def main():
    city = input('\nEnter your city : ')

    # city_data(city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8af2aa7fa978da0c3dc608a85406875c&units=Imperial'.format(city)

    weather = requests.get(url)

    data = weather.json()

    temp = data['main']['temp'] #temperature data
    wind_speed = data['wind']['speed'] #windspeed data
    wind_direction = data['wind']['deg'] #wind direction
    direction_card = wind_cardinal(wind_direction) #obtains cardinal wind direction
    description = data['weather'][0]['description'] #weather description

    print_info(temp, wind_speed, wind_direction, direction_card, description)

# def city_data(city): #I dont know how to use try/except
#     try:
#         url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8af2aa7fa978da0c3dc608a85406875c&units=Imperial'.format(city)

#         weather = requests.get(url)

#         data = weather.json()

#         temp = data['main']['temp'] #temperature data
#         wind_speed = data['wind']['speed'] #windspeed data
#         wind_direction = data['wind']['deg'] #wind direction
#         direction_card = wind_cardinal(wind_direction) #obtains cardinal wind direction
#         description = data['weather'][0]['description'] #weather description
#     except:
#         print('\nNot a valid city name, please check spelling.\n')
#     finally:
#         print_info(temp, wind_speed, wind_direction, direction_card, description)

def wind_cardinal(degree):
    '''Cardinal direction conversion'''
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

def print_info(temp, wind_speed, wind_direction, direction_card, description):
    '''Prints obtained data'''
    print('\nTemperature : {} F'.format(temp))
    print('Wind Speed : {} mph'.format(wind_speed))
    print('Wind Direction : {}° : {}'.format(wind_direction, direction_card))
    print('Weather Description : {}\n'.format(description.title()))

    while True:
        x = input('Would you like to search again? Y/N \n> ').lower()
        if x == 'y':
            main()
        elif x == 'n':
            goodbye()
            break
        else:
            print('Unsupported input')

def goodbye():
    print('\nGoodbye!\n')

main()