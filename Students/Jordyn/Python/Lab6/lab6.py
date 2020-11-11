'''
values and lists:
    -list of random characters
    -10 character loop
    -
'''

import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
punctuation = string.punctuation
# print(lower_case) #Testing print
# print(random.choice(lower_case)) #Testing print

password = ''
repeater = 0
repeat = int(input('How long would you like your password to be?\n>'))
while repeater < repeat:
    random_string = random.randint(1,3)
    if random_string == 1:
        password_add = random.choice(lower_case)
        password += password_add
        # print(password) #Testing print
        repeater += 1
    elif random_string == 2:
        password_add = random.choice(upper_case)
        password += password_add
        # print(password) #Testing print
        repeater += 1
    elif random_string == 3:
        password_add = random.choice(punctuation)
        password += password_add
        # print(password) #Testing print
        repeater += 1

print(f'Your {repeat} digit password has been generated:\n{password}')