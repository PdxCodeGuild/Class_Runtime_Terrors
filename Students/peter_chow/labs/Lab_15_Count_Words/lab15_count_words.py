#!/bin/python3
# Filename: lab15_count_words.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 15: Count Words - Version 1
# Date: 10/19/2020
# Version 1.0

'''
Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.

'''

import requests
import string
# Get text from URL
response = requests.get('http://www.gutenberg.org/cache/epub/51804/pg51804.txt')
response.encoding = 'utf-8' # Encode to 8 bits for using different text length
lower_character = response.text.lower() # Change to all lower characters
words_list = (lower_character.split()) # Returns a list of the words in the string/line , separated by the delimiter string.

print('\nTop 10 words and counts from the EBook of "Plague of Pythons":\nhttp://www.gutenberg.org/cache/epub/51804/pg51804.txt')
i = 0 # Set count to zero
for lines in words_list:
    lines.strip() # Removes both leading and trailing characters

counter_dict = {} # Create a dictionary for counts
for line in words_list:
    if line in counter_dict:
        counter_dict[line] += 1

    elif line not in counter_dict:
        counter_dict[line]= 1

#print (counter_dict)
words = list(counter_dict.items()) # Convert to a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True) # Sort highest to lowest count.
for w in range(min(10, len(words))):  # Print the top 10 words
    print(words[w])