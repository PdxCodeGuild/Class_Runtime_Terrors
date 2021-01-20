'''
Written by James Keicher
This is a Cadillac Jack production
10/15/2020
'''

# I chose specific methods as opposed to entire modules
#   simply be cause I haven't used that before
from string import ascii_lowercase as lower #Lowercase English alphabet 
from string import ascii_uppercase as upper #Uppercase English alphabet
from string import punctuation as punct #Printable punctuations
from random import randint #Generate random integer in range(a,b)
from random import choice #Randomly select one character from a set/list
from random import shuffle #Shuffle(some_list) will rearrange a list

password = [] # Blank list to be populated later

# Line 19 asks the user if they'd like to use the program
initiate = input("Would you like to generate a random password? y/n : ")
# Line 22 is the begining of the program.
#  If the user enters "y", program will run
if initiate == "y":
    up_case = input("How many uppercase letters would you like to use? : ")
    up_case = int(up_case) 
    low_case = input("How many lowercase letters would you like to use? : ")
    low_case = int(low_case)
    pun = input("How many special characters would you like to use? : ")
    pun = int(pun)
    num = input("How many numbers would you like to use? : ")
    num = int(num)
    length = num + pun + low_case + up_case

    for i in range(up_case):
        password += choice(upper)
    for i in range(low_case):
        password += choice(lower)
    for i in range (pun):    
        password += choice(punct)
    for i in range(num):
        password += str(randint(0,9))
    
    shuffle(password) 
    final_password = ''.join(password)
    print(f"Your random password is : {final_password}")


elif initiate == "n":
    print('''
Thank you for using my password generator. 
Have a nice day, Goodbye!''')
else:
    input('''
    Please enter a "y for Yes, or a "n" for No : ''')