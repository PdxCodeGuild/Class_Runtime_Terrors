# PDX Fullstack lab 15 version 1
# Word Count
# prints top 10 words of a given book

import string
hold = {}

def build_dict(word):
    if word in hold:
        hold[word] += 1 
    else:
        hold[word] = 1 


def main():

    with open ('adonais.txt', 'r', encoding ='utf-8') as file:
        lowertext = file.read().lower()
        exclude = set(string.punctuation)
        striptext = ''.join(ch for ch in lowertext if ch not in exclude)
        listtext = list(striptext.split(" "))
        
    
        i = 0
        hold = {}
        while i < (len(listtext)):
            # build dictionary
            #print(listtext[i])
            word = listtext[i]
                   
            if word in hold:
                hold[word] += 1 
            else:
                if word != '':
                    hold[word] = 1
            i += 1

        #print(hold)
        words = list(hold.items())
        words.sort(key=lambda tup: tup[1], reverse=True)
        for i in range(min(10, len(words))):
            print(words[i])

main()