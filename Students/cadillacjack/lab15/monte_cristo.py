from string import punctuation as punct

with open ('monte_cristo.txt', 'r') as document:
    document_content = document.read()
doc_cont = document_content.replace('\n',' ')

doc_cont.strip(punct)

for punc in punct:
    doc_cont = doc_cont.replace(punc, "")
    
doc_cont = doc_cont.lower()

word_list = doc_cont.split(' ')

for word in word_list:
    if word == '':
        word_list.remove(word)

word_count = {}

for word in word_list:
    if word not in word_count:
        word_count[word] = 1
    elif word in word_count:
        word_count[word] +=1 

words = list(word_count.items())

def sort_list(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tup [j][1] > tup[j +1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

newest_list = (sort_list(words))
newest_list = newest_list[::-1]

final_list = newest_list[:10]

print(newest_list[:10])