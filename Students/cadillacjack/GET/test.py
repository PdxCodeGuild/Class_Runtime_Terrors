import requests
from random import choice

categories = ["animal", "career", "celebrity", "dev", "fashion",
"food", "history","money", "movie", "music", "political",
"religion", "science", "sport", "travel"]

pick = choice(categories)



my_site = requests.get (f'https://api.chucknorris.io/jokes/random?category={pick}')

data = my_site.json()

print(data["value"])