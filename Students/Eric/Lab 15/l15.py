import string

with open ('book.txt', encoding='utf-8') as document:
    document_content = document.read()
    wordslist = document_content #Book to Var
    wordslist = wordslist.strip() # Remove all lines and spaces
    wordslist = wordslist.lower() # lower case all words
    wordslist = wordslist.split()  # split into words
    

worddic = dict() # Eypty Dictionary

for x in wordslist: #loop all the workds
    if x in worddic: #Key in the diction plus one
        worddic[x] = worddic[x] + 1
    else: 
        worddic[x] = 1 # Make new key
        
worddic =sorted(worddic.items(), key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(worddic))):  # print the top 10 words, or all of them, whichever is smaller
    print(worddic[i])
