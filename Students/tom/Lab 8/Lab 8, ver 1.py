# Lab 8: Version #1, Guess the Number
# 10/15/2020
# Tom Schroeder

import random

trys = 1

computer_number = random.randint(1,10)

print ('\nI\'ve chosen a number. Can you guess it?')

while trys < 11:
    user_guess = int(input ('\nWhat is your guess?\n'))
    if user_guess != computer_number:
        print ('Wrong. Try again.')
        trys += 1
    
    else:
        print (f'You guessed right! It took you {trys} time(s).')
        break

if trys == 11:
    print ('You\'ve guessed wrong too many times. Good bye.')
