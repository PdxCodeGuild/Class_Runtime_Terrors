


import requests
import json

response = requests.get('https://cat-fact.herokuapp.com/facts')

data = json.loads(response.text)
data = response.json()
for fact in data['all']:
    print(fact['text'])
    if 'user' in fact:
        print(fact['user']['name']['first'] + ' ' + fact['user']['name']['last'])
    else:
        print('No user')
    print()


# headers = {'Accept': 'text/plain'}
# response = requests.get('https://icanhazdadjoke.com/', headers=headers)
# print(response.text)

# headers = {'Accept': 'application/json'}
# response = requests.get('https://icanhazdadjoke.com/', headers=headers)
# data = response.json()
# print(data['joke'])





# term = input('what is the term you\'d like to search for? ').lower()
# page = 1
# while True:
#     params = {'page': page, 'term': term}
#     headers = {'Accept': 'application/json'}
#     # response = requests.get('https://icanhazdadjoke.com/search?term=' + term + '&page=' + page)
#     response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params=params)
#     print(response.url)
#     # print(response.text)
#     data = response.json()
#     # print(data)
#     for joke in data['results']:
#         print(joke['joke'])
#     total_pages = data["total_pages"]
#     print(f'Page {page}/{total_pages}')
#     next_page = input('would you like to see the next page? ').lower().strip()
#     if next_page in ['y', 'yes', 'ok', 'sure']:
#         page += 1
#     else:
#         break



# def get_country_from_currency(currency):
#     response = requests.get('https://restcountries.eu/rest/v2/currency/' + currency)
#     data = response.json()
#     return [row['name'] for row in data]

# from_amount = float(input('what is the amount? '))
# from_currency = input('what is the currency?').upper().strip()
# print(get_country_from_currency(from_currency))
# to_currency = input('what is the currency you\'d like to convert to?').upper().strip()
# print(get_country_from_currency(to_currency))

# response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': from_currency})
# rates = response.json()['rates']
# to_amount = rates[to_currency]*from_amount
# print(f'{from_amount} {from_currency} is {to_amount} {to_currency}')





