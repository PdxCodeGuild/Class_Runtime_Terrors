# 10/21/2020

import requests
import string
response = requests.get('http://www.gutenberg.org/cache/epub/22210/pg22210.txt')
response.encoding = 'utf-8'
book_content = response.text

result = string.punctuation
print(result)
for char in book_content:
    if char in result:
        char = char.replace(char,"")




# book_content = book_content.lower() # Make everything lower case
book_list = book_content.split(" ")
print(book_list)







# with open ("\\wsl$\Ubuntu-20.04\home\uzumakiniu\Class_Runtime_Terrors\Students\Ben\Lab_15_Count_Words\Forbidden_Land.txt","r", encoding='utf-8') as file:
#     text = file.read()
# print(text) 