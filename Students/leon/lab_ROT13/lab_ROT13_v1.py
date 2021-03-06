# PDX Fullstack lab 09 ROT13 version 1
# take user input as plaintext and output ciphertext
# using rotation of the encryption 13

import string
import copy

def caesar(alpha):
    global zeda
    global key

    foo = {}
    s = 96
    i = 0
    for i in range(len(zeda)):
        s = s + 1
        foo[(zeda[i])] = s
    #print(foo)
    #print((alpha) in foo)
    #print(foo.get(alpha))
    delta = (foo.get(alpha)) +key
    if delta > 122:
        delta = delta - 26

    poo = {}
    t = 96
    j = 0
    for j in range(len(zeda)):
        t = t + 1
        poo[t] = (zeda[j])
    #print(poo)
    nova = poo[delta]
    #print(nova)
    return(nova)
      
def main():
        global zeda
        global key
        bull = False
        

        while not bull:
            tag = True
            print("Welcome to Cypher 1.0\n")
            print("Key value = 13. Can only accept lowercase alphabeticals.\n")
            plain = input("Enter word to encrypt: ").lower()
            # convert str to list
            plain = (list(plain))
            n = len(plain)
            # test for validity of data
            for h in range(n):
                if plain[h] not in zeda:
                    tag = False
                
            if tag:
                bull = True
            
        key = 13
        # convert plain text to cipher text 
        # call function with each index of list
        cipher = copy.copy(plain)
          
        i = 0
        for i in range(len(plain)):
            cipher[i] = caesar(plain[i])
            i += 1

        # convert list to str
        print(str(cipher))

zeda = list(string.ascii_lowercase)
key = 0
main()