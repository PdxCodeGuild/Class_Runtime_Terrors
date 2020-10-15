# Password Generator
# 10/14/2020
# Tom Schroeder


import random
import string

another_password = 'Y' # sets variable for 'while' loop

while (another_password == 'Y'):

    print('\nI\'ll generate a password for you.\n')

    # user is prompted to enter the number and letter password length
    number_characters = input ('How many numbers would you like in your passord?\n')
    while number_characters.isdigit() == False:
        number_characters = input ('\nPlease enter a positive whole number. How many numbers would you like in your passord?\n')

    lower_characters = input('\nHow many lower case letters would you like in your password?\n')
    while lower_characters.isdigit() == False:
        lower_characters = input ('\nPlease enter a positvie number. How many lower case letters would you like in your password?\n')
    
    upper_characters = input('\nHow many upper case letters would you like in your password?\n')
    while upper_characters.isdigit() == False:
        upper_characters = input ('\nPlease enter a positvie number. How many upper case letters would you like in your password?\n')
    
    special_characters = input('\nHow many special characters would you like in your password?\n')
    while special_characters.isdigit() == False:
        special_characters = input ('\nPlease enter a positvie number. How many special characters would you like in your password?\n')
    
    password = []

    # password list as appended with a random digit the number of times selected by the user 
    number_count = 0
    while (number_count < int(number_characters)):
        numbers = random.choice (string.digits)
        password.append(numbers)
        number_count += 1
    
    # password list as appended with a random lower case letter the number of times selected by the user
    lower_count = 0
    while (lower_count < int(lower_characters)):
        lowers = random.choice (string.ascii_lowercase)
        password.append(lowers)
        lower_count += 1
    
    # password list as appended with a random upper case letter the number of times selected by the user
    upper_count = 0
    while (upper_count < int(upper_characters)):
        uppers = random.choice (string.ascii_uppercase)
        password.append(uppers)
        upper_count += 1

    # password list as appended with a random special character the number of times selected by the user
    special_count = 0
    while (special_count < int(special_characters)):
        specials = random.choice (string.punctuation)
        password.append(specials)
        special_count += 1


    # values is password list are shuffled randomly
    random.shuffle (password)

    # characters in the password list are joined into a string and printed
    seperator = ''
    password = seperator.join (password)
    print (f'\nYour password is: {password}\n')
    
    #user is asked if they would like to generate another password or exit the program
    another_password = input ('Would you like to generate another password? Y or N\n').capitalize()

    while another_password!= 'Y' and another_password != 'N':
        another_password = input ('Only enter Y or N. Would you like to generate another password? Y or N\n').capitalize()