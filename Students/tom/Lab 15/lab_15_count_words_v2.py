# word count lab
# October 21, 2020
# Tom Schroeder

import string

word_list = [] # initiates variable for a list of all words in the book
word_pairs = []
word_pair_dictionary = {}

with open ('pg63523.txt', 'r') as book: # opens text file of book
    number_of_characters = 100 # sets variable to limit of characters
    text = book.read() # limits file characters for testing
    text = text.lower() # changes all upper case characters to lower case

    # loop that replaces all non-ascii characters with a space
    for characters in text:
        if characters not in string.ascii_letters:
            text = text.replace(characters, " ")

    words = text.split() # splits the string into a list

    number_of_words = len(words) # sets variable value to the number of words in the text
    first = 0  # initiates variable to start at first element of the list of words for the first word in the word pair
    second = 2 # initiates variable to start at second element of the list of words for the second word in the word pair
    i = 0 # initiates counter for while loop

    # loop to join each word with the subsequent word seperated by the space character
    while i < number_of_words:
        word_pairs.append(' '.join(words[first:second]))
        first += 1
        second += 1
        i += 1    

    # for each word-pair in the word_pairs list...
    for word_pair in word_pairs:
        if word_pair in word_pair_dictionary:
            word_pair_dictionary[word_pair] += 1 # if word-pair key is in dictionary increments value by 1
        else:
            word_pair_dictionary[word_pair] = 1 # if word-pair not in dictionary adds key and sets value to 1 

    word_pair_tuple = list(word_pair_dictionary.items()) # converts dictionary of word-pairs to a list

    word_pair_tuple.sort(key=lambda tup: tup[1], reverse=True) # sorts value of dictionary key/value pairs from highest to lowest


    print ('\nThe top ten word-pairs in this text are:\n')
    for i in range(min(10, len(word_pair_tuple))):  # print the top 10 word-pairs, or all of them, whichever is smaller
        print(word_pair_tuple[i])