import string
import operator

punctuations = string.punctuation
word_list = {}

with open('lab15_read.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            for char in word:
                if char in punctuations:
                    word = word.replace(char, '')
        if word in word_list:
            word_list[f'{word}'] += 1
        elif word not in word_list:
            word_list[word] = 1

word_list = sorted(word_list.items(), key=operator.itemgetter(1), reverse=True) #sorts list into tuples without use of Lambda

print('Top 10 words in file:\n')
for key in range(0, 10): #Prints out the top 10 most used words from file.
    word_list_range = word_list[key]
    word = word_list_range[0]
    repeat = word_list_range[1]
    print(f'{key}. Word : \'{word.capitalize()}\' | Repeated : {repeat}')

    