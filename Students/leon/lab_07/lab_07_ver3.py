# PDX Fullstack Lab 07 version 3
# generate a password of length given by user
# and user determines how many .lower, .upper, .special, and digits are in the password

import random
import string

def main():
    password = ''
    n = input("Enter password length: ")
    n = int(n)
    l = input("How many lower: ")
    l = int(l)
    if (n - l) > 0: 
        print("You have ", n-l, " spots remaining.\n")
        u = input("How many upper: ")
        u = int(u)
        if (n - l - u) > 0:
            print("You have ", n - l - u, " spots remainig.\n")
            s = input("How many special: ")
            s = int(s)
    else: 
        u = 0
        s = 0
    d = (n - l - u - s)
    if d < 0:
        d = 0
    
    # counter variables:
    # i counts n, j counts l, k counts u, m counts s, p counts d
    i = 0
    j = 0
    k = 0
    m = 0
    p = 0

    while i < n:
        if n > 0: 
            while j < l:
                char = random.choice(string.ascii_lowercase)
                password += char
                j = j + 1
        if u > 0:
            while k < u:
                char = random.choice(string.ascii_uppercase)
                password += char
                k = k + 1
        if s > 0: 
            while m < s:
                char = random.choice(string.punctuation)
                password += char
                m = m + 1
        if d > 0: 
            while p < d:
                char = random.choice(string.ascii_lowercase)
                password += char
                p = p + 1
        
        i = i + 1
    
    random.shuffle(list(password))
    print(password)




main()