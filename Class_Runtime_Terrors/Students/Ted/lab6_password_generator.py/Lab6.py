

import random

#generate a password of length n using a while loop
#and random.choice to get a string aof random numbers
#use input,print,looping,random.choice...
#the string builder pattern
choices = [1,2,3,4,5,6,7,8,9,0]

pword = ""
length = int(input('How long a password do you need? '))
i = 0
while i < length:
    pword = pword + str(random.choice(choices))
    i += 1

print (f'Your random number is: {pword}')

