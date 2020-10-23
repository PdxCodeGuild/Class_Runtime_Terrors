'''
Written by James Keicher
This is a Cadillac Jack production
Completed 10/23/20
'''

import requests
from string import punctuation as punct
# Importing modules needed for code

response = requests.get('https://www.gutenberg.org/files/45484/45484-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
# Pull book from website "gutenberg.org"
# Encode book into utf-8 format so we can manipulate it

poe = response.text
# Save contents of book to variable "poe"

unwanted = ("\n \r \t" + punct)
# Create variable with escape characters and punctuation

poe = poe.strip(unwanted).lower().split(" ")
# Remove all punction and escape characters,
# Lowercase every word, Separate each word with space

raven = {}
# Create blank dictionary

for i in poe:
    if i == "":
        continue 
    elif i not in raven:
        raven[i] = 1
    elif i in raven:
        raven[i] += 1
# Iterate through book, after skipping blank strings,
# Check if a word is in "raven", if word in "raven",
# Add 1 to value of word, if not in "raven", 
# Add to "raven" with value of 1

raven = list(raven.items())
# Change dictionary "raven" into a list of tuples

raven.sort(key = lambda tup: tup[1], reverse = True)
# Sort "raven" by index, reorder high to low

print(raven[:10])
# Print out top 10 words in Edgar Allen Poe's "The Raven"