# Cleon

import string 
import random

speChar = string.hexdigits + string.punctuation # special characters

print(" Welcome to my first password generator  \n") # Welcome message 
lower_case_length = int(input("Please use the number pad to enter how many lowercase letters : ")) 
upper_case_length = int(input("How many uppercase letters : ")) 
number_length = int(input("How many numbers : "))  
special_length = int(input("How many special characters : ")) 

gP = ""
while True:
    while lower_case_length > 0:
        gP += random.choice(string.ascii_lowercase)
        lower_case_length = lower_case_length - 1
    while upper_case_length > 0:
        gP += random.choice(string.ascii_uppercase)
        upper_case_length = upper_case_length - 1
    while number_length > 0:
        gP += random.choice(string.digits)
        number_length = number_length - 1
    while special_length  > 0:
        gP += random.choice(speChar)
        special_length  = special_length  - 1
    break

gP = (random.sample(gP, len(gP))) # Can't randomly sort string elements.Use this function it returns as a list 
gP= ''.join(gP) # Then you must join function to convert back to string 
print(gP) 

    
    




