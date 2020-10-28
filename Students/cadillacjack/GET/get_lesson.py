import requests

# my_site = requests.get (f'https://api.chucknorris.io/jokes/random?category={"religion"}')

# data = my_site.json()

cate = requests.get(f'https://api.chucknorris.io/jokes/categories')

catego = cate.json()

print(catego)

# print(data["value"])
