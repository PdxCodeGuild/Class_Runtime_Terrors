# Given an input string of a certain length, design an algorithm that compresses the string. The string should be compressed such that consecutive duplicates of
#  characters are replaced with the character and followed by the number of consecutive duplicates.
# For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3dex6".


def test(wordlist):
    wordlist = wordlist
    letter_dic = dict()
    answerlist= []
    for x in wordlist: #loop all the letters
        if x in letter_dic: #Key in the diction plus one
            letter_dic[x] = letter_dic[x] + 1
        else: 
            letter_dic[x] = 1 # Make new key

    for k,v in letter_dic.items(): # Calling up Keys and Values
        answerlist.append(k)
        if v != 1:
            vstring =str(v) # Need to make int to Str otherwises unable to join
            answerlist.append(vstring)
    return ("".join(answerlist))

print(test('wwwwaaadexxxxxx'))