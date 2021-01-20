def rot(word,rot):
    wordlist = list(word)
    answerlist =[]
    rot = rot
    for x in range(len(wordlist)):
        newasc = ord(wordlist[x]) #Char to ascii valve
        if (newasc >= 97 and newasc <=122) or (newasc >= 65 and newasc <=90):
            if ((newasc + rot) >= 123 ):
                newasc -= rot
            else:
                newasc += rot
            answerlist.append(chr(newasc))
        else:
            answerlist.append(chr(newasc))

    return answerlist #Return ascii valve to char

print("Welcome to the Rot 13 Cipher")
userinput = input('Input your password to be cipher: ')
x = (rot(userinput, 13))
x =("".join(x))
print (x)