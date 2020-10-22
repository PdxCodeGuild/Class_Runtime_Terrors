import requests
import time

zip = input('What is the Zip code for your weather request?\n')

current_wx_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip}&units=imperial&appid=API')
current_wx_data = current_wx_response.json()

temp           = current_wx_data ["main"]["temp"]
feels_temp     = current_wx_data ["main"]["feels_like"]
temp_max       = current_wx_data ["main"]["temp_max"]
temp_min       = current_wx_data ["main"]["temp_min"]
humidity       = current_wx_data ["main"]["humidity"]
wind_speed     = current_wx_data ["wind"]["speed"]
wind_direction = current_wx_data ["wind"]["deg"]
city           = current_wx_data ["name"]

def convert_unix_to_time (time_tuple):
    time_indices = [3,4] # indices for hours and minutes 
    time_elements = [time_tuple[index] for index in time_indices] # converts tuple to list
    time_list = map(str, time_elements) # converts list of integers to strings
    seperator = ':' # separator for hours and minutes
    formatted_time = seperator.join(time_list) # creates hh:mm
    return formatted_time

def convert_unix_to_date (date_tuple):
    date_indices = [1,2,0] # indices for month, day, and year
    date_elements = [date_tuple[index] for index in date_indices] # converts tuple to list
    date_list = map(str, date_elements) # converts list of integers to strings
    seperator ='/' # character that deliniates month, day, and year
    formatted_date = seperator.join(date_list) # creates mm/dd/yyy
    return formatted_date

date_time_info_tuple = time.localtime(current_wx_data["dt"]) # tuple of date/time of current weather reading

time_formatted = convert_unix_to_time(date_time_info_tuple) # calls function to format time of current weather reading

date_formatted = convert_unix_to_date(date_time_info_tuple) # calls function to format date of current weather reading

sunrise_info_tuple  = time.localtime(current_wx_data["sys"]["sunrise"]) # tuple of sunrise elements
sunrise_time_formatted = convert_unix_to_time(sunrise_info_tuple) # calls function to format time of sunrise

sunset_info_tuple = time.localtime(current_wx_data["sys"]["sunset"]) # tuple of sunset elements
sunset_time_formatted = convert_unix_to_time(sunset_info_tuple) # calls function to format time of sunset

sky_conditon_list = (current_wx_data ['weather']) # assigns variable to a list with the value at key "weather"
sky_condition_dictionary = sky_conditon_list[0] # assigns variable the dictionary at position 0 in the list
sky_condition = sky_condition_dictionary["description"] # assigns variable the value at key "description"
 
print (f'\nThis is the current weather conditions as of {time_formatted} on {date_formatted}.\n')
print (f'For the city of {city}, the wind speed is {wind_speed} mph from {wind_direction} degrees.\n')
print(f'The temperature is {temp} degrees F, which feels like {feels_temp} degrees F.\n')
print (f'The hmuidity is {humidity} percent.\n')
print(f'The maximum temperature is {temp_max} degrees F and the minimum temperature is {temp_min} degrees F.\n')
print (f'The sky condition is "{sky_condition}".')