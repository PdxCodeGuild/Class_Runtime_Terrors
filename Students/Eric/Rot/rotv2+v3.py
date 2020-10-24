def rot(word,rot):
    wordlist = list(word)
    answerlist =[]
    rot = rot
    for x in range(len(wordlist)):
        newasc = ord(wordlist[x]) #Char to ascii valve
        if (newasc >= 97 and newasc <=122) or (newasc >= 65 and newasc <=90):
                if (newasc >= 97 and newasc <=122):
                    if ((newasc + rot) >= 123 ):
                        newasc -= rot
                        answerlist.append(chr(newasc))
                    else:
                        newasc += rot
                        answerlist.append(chr(newasc))
                else:
                    if ((newasc + rot) >= 91):  
                        newasc -= rot
                        answerlist.append(chr(newasc))
                    else:
                        newasc += rot
                        answerlist.append(chr(newasc))
        else:
            answerlist.append(chr(newasc))

    return answerlist #Return ascii valve to char

print("Welcome to the Rot Cipher")
userinput = input('Input your password to be cipher: ')
userrot =  input('Input your Rot: ')
userrot = int(userrot)

x = (rot(userinput, userrot))
x =("".join(x))
print (x)