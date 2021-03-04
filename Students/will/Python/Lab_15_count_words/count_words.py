import string
f = "C:/Users/17196/Desktop/345.txt"

with open (f, 'r') as document:
    document_content = document.read()
    document_content = document_content.lower()

punctuation = list(string.punctuation)
document_content = list(document_content)

no_punc = []
for char in document_content:
    if char not in punctuation:
        no_punc.append(char)
no_punc = str(''.join(no_punc))
no_punc.replace('\n', '')
no_punc.replace('  ', ' ')
word_list = no_punc.split('\n')
word_list = r' '.join(word_list)
word_list = word_list.split(' ')

word_dict = {}
for word in word_list:
    if word not in word_dict:   
        word_dict[word] = 1
    if word in word_dict:
        count = word_dict[word]
        word_dict[word] = count + 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(25, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
#print(sorted(word_dict.values()))