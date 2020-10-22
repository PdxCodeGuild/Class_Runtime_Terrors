import string

punctuations = string.punctuation
# print(punctuations)
word_list = {}

no_punct_word = ''

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

word_list = sorted(word_list.items(), key = lambda x: x[1], reverse=True) #stolen and I dont fully understand yet... sorry

# print(word_list)
print('Top 10 words in file:\n')

for key in range(0, 10):
    # for word, repeat in word_list[key]:
    word_list_range = word_list[key]
    word = word_list_range[0]
    repeat = word_list_range[1]
    print(f'{key}. Word : \'{word.capitalize()}\' | Repeated : {repeat}')