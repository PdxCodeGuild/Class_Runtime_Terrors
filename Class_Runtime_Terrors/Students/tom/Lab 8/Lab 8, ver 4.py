# Lab 8: Version #4, Guess the Number, unlimted trys, and with closer clue
# 10/15/2020
# Tom Schroeder

import random

trys = 1 # initializes count of trys
current_difference = 0 # initializes variable showing the difference between the computer's number and the user's guess

computer_number = random.randint(1,10) # computer generates random number between 1 an 10
print (f'Computer Number is {computer_number}\n')

print ('\nI\'ve chosen a number between 1 an 10. Can you guess it?')

# loop to allow user to continue to guess until answering correctly or opting to quit
while True:
    
    past_difference = current_difference
    
    user_guess = input ('\nWhat is your guess?\n')
    
    # loop to verify input is a digit
    while user_guess.isdigit() == False:
        user_guess = input (f'\n"{user_guess}" is not a valid entry. What is your guess?\n')

    user_guess = int(user_guess)

    current_difference = abs(user_guess - computer_number)

    # if guess is wrong user can try again
    if user_guess != computer_number:
        if past_difference == 0:
            play_again = input (f'Your guess of {user_guess} is incorrect. Would you like to try again?. "Y" or "N"\n').capitalize()

        elif current_difference < past_difference:
            play_again = input (f'Your guess of {user_guess} is closer to the answer. Would you like to try again?. "Y" or "N"\n').capitalize()
        
        elif current_difference > past_difference:
            play_again = input (f'Your guess of {user_guess} is further from the answer. Would you like to try again?. "Y" or "N"\n').capitalize()

        else:
            play_again = input (f'Your guess of {user_guess} is the same as your previous entry. Would you like to try again?. "Y" or "N"\n').capitalize()
              
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