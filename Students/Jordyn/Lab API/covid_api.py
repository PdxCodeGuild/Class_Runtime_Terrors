#Covid-19 API

import requests

def get_country_names():
    '''Retrieves all available Country names'''
    url = 'https://api.covid19api.com/countries'
    url_get = requests.get(url)
    data = url_get.json()
    country = []
    for key in range(len(data)):
        country += [data[key]["Country"]]
    return sorted(country)

def get_country_codes():
    '''Retrieves all available Country ID\'s'''
    url = 'https://api.covid19api.com/countries'
    url_get = requests.get(url)
    data = url_get.json()
    country_code = []
    for key in range(len(data)):
        country_code += [data[key]["ISO2"]]
    return sorted(country_code)

def get_country_info(data, country_selection):
    '''Retrieves data for specific Country'''
    data = data["Countries"]
    for key in range(len(data)):
        for temp_data in data[key].values():
            if temp_data == country_selection:
                return data[key]
            # elif temp_data == country_id:
            #     return data[key]

def format_data():
    print()

print("Gathering Current Covid-19 Related Data")

url = 'https://api.covid19api.com/summary'
url_get = requests.get(url)
data = url_get.json()

countries = get_country_names()
country_id = get_country_codes()

print("Success.\n")

while True:
    print("             COVID-19 Related Information Live\n")
    country_selection = input("""Please input the name of the Country you are searching for. If you know your Country ID, you may also input that.
If you would like a list of available Countries, type 'Country List'.\n> """)
    while country_selection not in countries or country_selection not in country_id:
        country_selection = input("""\nSelection not available. Please ensure correct spelling and Capitalization.

Please input the name of the Country you are searching for. If you know your Country ID, you may also input that.
If you would like a list of available Countries, type 'Country List'.\n> """)
        if country_selection in countries or country_selection in country_id:
            break
    if country_selection == 'County List':
        print(countries)
    
    country_info = get_country_info(data, country_selection)
    print(country_info)