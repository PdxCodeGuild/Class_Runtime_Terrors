# PDX Fullstack Lab 07 version 1
# generate a password of length n 

import random
import string

def main():
    password = ''
    n = random.randint(4,16)
    i = 0
    
    while i < n:
        char = random.choice(string.ascii_letters + string.digits)
        password += char
        i = i + 1

    print(password)




main()