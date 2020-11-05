from string import punctuation as punct
# Import ascii punctuation as "punct".
# "punct" is a list of strings

with open ('monte_cristo.txt', 'r') as document:
    document_content = document.read(500)
doc_cont = document_content.replace('\n',' ')
# Open designated file as "file". "file" is a string

for punc in punct:
    doc_cont = doc_cont.replace(punc, "")
    # Remove all punctuation from string
    
doc_cont = doc_cont.lower()
# Lowercase all words

doc_cont = doc_cont.split(' ') 
# Convert string to list of strings

word_count = {} # Create empty dictionary

for word in doc_cont: # Scan "doc_cont", check every word.
    if word not in word_count: # If scanned word not in "word_count"...
        word_count[word] = 1 # Add word to "word_count" as a key with the value 1
    elif word in word_count: # If scanned word is in "word_count"...
        word_count[word] +=1  # Increase value of key "word" by 1

words = list(word_count.items())
# Convert dict "word_count" to a list of tuples.
# Save list as "words"
# Tuples are key, value pairs

words.sort(key = lambda tup: tup[1],reverse = True)
# Sort list "words" using the value of each tuple
# Reverse the order of list fro highest value to lowest

print(f"The top ten words are ; {words[:10]})")
# print the first 10 words of list "words"