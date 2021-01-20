# word count lab
# October 21, 2020
# Tom Schroeder

import string


user_word = input ('Enter a word and I\'ll show you the words which most frequently follow it:')

with open ('pg63523.txt', 'r') as book: # opens text file of book
    number_of_characters = 100 # sets variable to limit of characters
    text = book.read() # limits file characters for testing
    text = text.lower() # changes all upper case characters to lower case

    for characters in text: # loop that replaces all non-ascii characters with a space
        if characters not in string.ascii_letters:
            text = text.replace(characters, " ")

    word_list = [] # initiates variable for a list of all words in the book
    word_list = text.split() # splits the string into a list

    
    words_list_length = len(word_list) # sets variable to length of list
    i = 0 # initiates incrementer to 0
    word_location = [] # initiates list to store loctaions of user's word
    while i < words_list_length: # loops through each word in the text
        if word_list[i] == user_word: # compares each word in the text to the user's word
            word_location.append(i+1) # if user's word is in the text the NEXT index location of that word is appended to the list
        i += 1

    following_words = [] # initiates list to store following words
    for i in word_location: # loops through each index location
        following_words.append(word_list[i]) # appends following words to the list

    # for each following word in the following word list...
    following_words_dictionary = {} # initiates variable for a dictionary of all following word in the book
    for following_word in following_words:
        if following_word in following_words_dictionary:
            following_words_dictionary[following_word] += 1 # if following word key is in dictionary increments value by 1
        else:
            following_words_dictionary[following_word] = 1 # if following word not in dictionary adds key and sets value to 1 

    following_word_tuple = list(following_words_dictionary.items()) # converts dictionary of following words to a list

    following_word_tuple.sort(key=lambda tup: tup[1], reverse=True) # sorts value of dictionary key/value pairs from highest to lowest


    print (f'\nThe top ten words following "{user_word}" in this text are:\n')
    for i in range(min(10, len(following_word_tuple))):  # print the top 10 following words, or all of them, whichever is smaller
        print(following_word_tuple[i])