"""

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
Allow the user to enter the value of n, remember to convert its type, as input returns a string.
"""

import random

def genPassword(n):
    p = ""
    c = 0
    while c < n:
        p = p + random.choice("abcdef12345")
        c = c + 1
    return p
def main():
    try:
        n = int(input("Enter the length: "))
        print(genPassword(n))
    except:
        print("error")
        exit(1)



if __name__ == '__main__':
    main()