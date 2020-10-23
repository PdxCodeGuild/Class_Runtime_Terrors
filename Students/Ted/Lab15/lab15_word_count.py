

#content = copied from
import requests
import string
response = requests.get('http://www.gutenberg.org/files/98/98-0.txt')
response.encoding = 'utf-8'
book_content = response.text.lower()

broke_lines = (book_content.split())
i = 0
for lines in broke_lines:
    lines.strip()

counter_dict = {}
for line in broke_lines:
    if line in counter_dict:
        counter_dict[line] += 1

    elif line not in counter_dict:
        counter_dict[line]= 1

#print (counter_dict)
words = list(counter_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

    
#print(broke_lines)

#book_content.strip(string.punctuation)
#make everything lower, done
#strip punctuation
#split into a list of words

#make a dictionary{} with the key as a word
#and the value as the number of words
#if word in dict add one to value, else add to dict with value of 1
#word_dict is a dictionary where the key is the word and the value is the count
#words = list(word_dict.items()) # .items() returns a list of tuples
#words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
#for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#    print(words[i])

#print (book_content)

    