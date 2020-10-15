# PDX Fullstack Lab 07 version 2
# generate a password of length given by user 

import random
import string

def main():
    password = ''
    n = input("Enter password length: ")
    n = int(n)
    i = 0

    while i < n:
        char = random.choice(string.ascii_letters + string.digits)
        password += char
        i = i + 1

    print(password)




main()