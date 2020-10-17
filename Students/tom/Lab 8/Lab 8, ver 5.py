# Lab 8: Version #4, Guess the Number, unlimted trys, and with closer clue
# 10/15/2020
# Tom Schroeder

import random

trys = 1 # initializes count of trys

user_number = input ('What number do you want the computer to guess?\n')
while user_number.isdigit() == False:
    user_number = input ('You entered an incorrect value. What number do you want the computer to guess?\n')

user_number = int(user_number)
computer_guesses = []

while user_number not in computer_guesses:
    computer_number = random.randint(1,100) # computer generates random number between 1 an 10
    # print (f'The computer\'s guess is {computer_number}')

    while computer_number in computer_guesses:
        computer_number = random.randint(1,100) # computer generates random number between 1 an 10

    if user_number != computer_number:
        computer_guesses.append(computer_number)
        trys +=1
        # input (f'The computer\'s list of guesses after adding new number to list is {computer_guesses} and {trys} trys')

    elif user_number == computer_number:
        print (f'The computer guessed {trys} times with the guesses of {computer_guesses} before guessing your entry of "{computer_number}".')
        break