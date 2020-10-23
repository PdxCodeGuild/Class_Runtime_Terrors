import string

with open ('book.txt', encoding='utf-8') as document:
    document_content = document.read()
    wordslist = document_content
    wordslist = wordslist.strip()
    wordslist = wordslist.lower()
    wordslist = wordslist.split() 
    

worddic = dict() 

for x in wordslist: 
    if x in worddic: 
        worddic[x] = worddic[x] + 1
    else: 
        worddic[x] = 1


worddic =sorted(worddic.items(), key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(worddic))):  # print the top 10 words, or all of them, whichever is smaller
    print(worddic[i])
