# Lab 8: Version #3, Guess the Number, unlimted trys, and too high/too low response
# 10/15/2020
# Tom Schroeder

import random

trys = 1 # initializes count of trys

computer_number = random.randint(1,10) # computer generates random number between 1 an 10

print ('\nI\'ve chosen a number between 1 an 10. Can you guess it?')

# loop to allow user to continue to guess until answering correctly or opting to quit
while True:
    user_guess = input ('\nWhat is your guess?\n')
    
    # loop to verify input is a digit
    while user_guess.isdigit() == False:
        user_guess = input (f'\n"{user_guess}" is not a valid entry. What is your guess?\n')

    user_guess = int(user_guess)

    # if guess is wrong user can try again
    if user_guess != computer_number:
        if user_guess < computer_number:
            play_again = input (f'Your guess of {user_guess} is too low. Would you like to try again?. "Y" or "N"\n').capitalize()
        
        elif user_guess > computer_number:
            play_again = input (f'Your guess of {user_guess} is too high. Would you like to try again?. "Y" or "N"\n').capitalize()
                
        # loop if user enters something other than Y or N to play again
        while play_again != 'Y' and play_again != 'N':
            play_again = input (f'"{play_again}" is an incorrect response. Would you like to try again?. "Y" or "N"\n').capitalize()
        
        # increments number of trys by one
        if play_again == 'Y':
            trys += 1

        # good bye message if player chooses to quit
        elif play_again == 'N':
            print ('\nThanks for playing. Good bye.')
            break

    # tells the user they guessed correctly and prints the number of attempts
    else:
        print (f'You guessed right! It took you {trys} time(s).')
        break