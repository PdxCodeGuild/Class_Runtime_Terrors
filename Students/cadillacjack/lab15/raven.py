import requests
from string import punctuation as punct

response = requests.get('https://www.gutenberg.org/files/45484/45484-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8

poe = response.text

unwanted = ("\n \r \t" + punct)
poe = poe.strip(unwanted).lower().split(" ")

raven = {}

for i in poe:
    if i == "":
        continue 
    elif i not in raven:
        raven[i] = 1
    elif i in raven:
        raven[i] += 1

raven = list(raven.items())

raven.sort(key = lambda tup: tup[1], reverse = True)

print(raven[:10])