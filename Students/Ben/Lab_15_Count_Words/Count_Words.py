# 10/21/2020

import requests
import string
response = requests.get('http://www.gutenberg.org/cache/epub/22210/pg22210.txt')
response.encoding = 'utf-8'
book_content = response.text


# for char in book_content:
#     if char in result:
#         print(char)
#         char = char.replace(char,"")

book_content = book_content.lower() # Make everything lower case
book_list = book_content.split(" ")

for element in range(len(book_list)):
    book_list[element] = book_list[element].strip(string.punctuation)
#   print(book_list)

word_count = 0 
for word in range(1,len(book_list)):
    # word indicate the index
    # book_list[word] indicate the actual "word"    
    if book_list[word] == book_list[0]:
        word_count += 1
    else:
        break
summary_dict = {}
summary_dict[book_list[0]] = word_count
print(summary_dict)











# with open ("\\wsl$\Ubuntu-20.04\home\uzumakiniu\Class_Runtime_Terrors\Students\Ben\Lab_15_Count_Words\Forbidden_Land.txt","r", encoding='utf-8') as file:
#     text = file.read()
# print(text) 