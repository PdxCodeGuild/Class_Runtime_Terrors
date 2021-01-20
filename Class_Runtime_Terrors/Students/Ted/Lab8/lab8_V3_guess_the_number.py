
#version 3

#computer guesses number 1-10
import random


comp_guess = random.randint(1,10)

user_guess = int(input("Guess what number, between 1 and 10, I am thinking. "))

x = 1
while True:
    if user_guess == comp_guess:
        print(f'Correct! You guessed it in  {x}  times.')
        break 
        
    elif user_guess > comp_guess:
        user_guess = int(input('Your guess was too high, try again. '))
    elif user_guess < comp_guess:
        user_guess = int(input('Your guess was too low, try again. '))
    x += 1

    #else:
        #print('Sorry, you have had your 10 trys, you lose.')
        #break
