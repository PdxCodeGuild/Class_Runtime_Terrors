# 10/14/2020
# input, print, looping, random.choice, the 'string builder pattern'
# Version 1
import random
import string

number_lower_case = input("How many lower case letters you want in the pw: ")
number_upper_case = input("How many upper case letters you want in the pw: ")
number_special_char = input("How many special charates you want in the pw: ")

password = []

a = 1
b = 1
c = 1

while a <= int(number_lower_case):
    password.append(random.choice(string.ascii_lowercase))
    a += 1
else:
    while b <= int(number_upper_case):
        password.append(random.choice(string.ascii_uppercase))
        b += 1
    else:
        while c <= int(number_special_char):
            password.append(random.choice(string.punctuation))
            c += 1
        else:
            exit

password = ''.join(password)
print(password)
