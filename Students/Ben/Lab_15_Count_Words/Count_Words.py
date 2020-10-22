# 10/21/2020

# import requests
# response = requests.get('http://www.gutenberg.org/cache/epub/22210/pg22210.txt')
# response.encoding = 'utf-8'
# print(response.text)

with open ('Forbidden_Land.txt', 'r', encoding ='utf-8') as file:
    text = file.read()
print(text) 