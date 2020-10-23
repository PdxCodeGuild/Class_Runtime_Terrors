#Cleon 
#Lab 15
#10-21-2020
#version 1

from collections import Counter
import string

with open ('book.txt', 'r',  encoding='utf-8') as document:
    document_content = document.read().lower()
    removed = string.punctuation
    for pun in document_content:
        if pun in removed: # removes punctuation
            document_content = document_content.replace(pun,"") #replaces punctuation removed and joins letters 
 
word_list = document_content.split() # splits words in lists
   
counts_words = Counter(word_list)  # counts equivalent values in list

Mostcommon = counts_words.most_common(10)  # Returns a list of the most common elements and their counts 
  
print("\n", Mostcommon) # print most common words and their counts 
