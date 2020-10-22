from string import punctuation as punct

with open ('monte_cristo.txt', 'r') as document:
    document_content = document.read(500)
doc_cont = document_content.replace('\n',' ')

for punc in punct:
    doc_cont = doc_cont.replace(punc, "")
    
doc_cont = doc_cont.lower()

doc_cont = doc_cont.split(' ')

word_count = {}

for word in doc_cont:
    if word not in word_count:
        word_count[word] = 1
    elif word in word_count:
        word_count[word] +=1 

words = list(word_count.items())

words.sort(key = lambda tup: tup[1],reverse = True)

print(f"The top ten words are ; {words[:10]})")