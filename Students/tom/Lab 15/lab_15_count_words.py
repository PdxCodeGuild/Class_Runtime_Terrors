# word count lab
# October 21, 2020
# Tom Schroeder

import string

word_list = [] # initiates variable for a list of all words in the book
word_dictionary = {}

with open ('pg63523.txt', 'r') as book: # opens text file of book
    number_of_characters = 500 # sets variable to limit of characters
    text = book.read() # limits file characters for testing
    text = text.lower() # changes all upper case characters to lower case

    # loop that replaces all non-ascii characters with a space
    for characters in text:
        if characters not in string.ascii_letters:
            text = text.replace(characters, " ")

    words = text.split() # splits the string into a list

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1


    word_tuple = list(word_dictionary.items())

    word_tuple.sort(key=lambda tup: tup[1], reverse=True)

    print ('\n')
    for i in range(min(10, len(word_tuple))):  # print the top 10 words, or all of them, whichever is smaller
        print(word_tuple[i])