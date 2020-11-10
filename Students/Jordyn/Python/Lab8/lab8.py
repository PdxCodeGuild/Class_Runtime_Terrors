'''
To-do: Version 1
- import random
- allow the user to make a guess
- keep track of used guesses
- congradulate on win and make the user aware of the times attempted
'''

# import random

# correct_number = random.randint(1,10)

# attempts = 0

# while attempts <= 10:
#     guess = int(input('Guess a number from 1 to 10!\n> '))
#     if guess == correct_number:
#         attempts += 1
#         print(f"Congradulations! {guess} was the correct number!\n You guessed {attempts} times.")
#         break
#     elif guess != correct_number:
#         attempts += 1
#         print("Guess again!")

'''
To-do: Version 2
- import random
- allow the user to make a guess
- keep track of used guesses
- congradulate on win and make the user aware of the times attempted
- now with unlimited guess attempts
'''

# import random

# correct_number = random.randint(1,10)

# attempts = 0

# while True:
#     guess = int(input('Guess a number from 1 to 10!\n> '))
#     if guess == correct_number:
#         attempts += 1
#         print(f"Congradulations! {guess} was the correct number!\n You guessed {attempts} times.")
#         break
#     elif guess != correct_number:
#         attempts += 1
#         print("Guess again!")

'''
To-do: Version 3
- import random
- allow the user to make a guess
- keep track of used guesses
- congradulate on win and make the user aware of the times attempted
- now with unlimited guess attempts
- tell user if they are too high or too low
'''

# import random

# correct_number = random.randint(1,10)

# attempts = 0

# while True:
#     guess = int(input('Guess a number from 1 to 10!\n> '))
#     if guess == correct_number:
#         attempts += 1
#         print(f"Congradulations! {guess} was the correct number!\n You guessed {attempts} times.")
#         break
#     elif guess != correct_number:
#         attempts += 1
#         if guess > correct_number:
#             print("Your guess is too high!")
#         elif guess < correct_number:
#             print("Your guess is too low!")

'''
To-do: Version 4
- import random
- allow the user to make a guess
- keep track of used guesses
- congradulate on win and make the user aware of the times attempted
- now with unlimited guess attempts
- tell user if they were closer to the correct answer
- get absolute difference between current and previous guess.
'''

# import random

# correct_number = random.randint(1,10)
# attempts = 0
# last_guess = 0

# while True:
#     guess = int(input('Guess a number from 1 to 10!\n> '))
#     absolute_difference = abs(correct_number - guess) #Gives the absolute value of the difference between your guess and the correct number
#     if guess not in range(1,11):
#         print("Not a number between 1-10.")
#     elif guess == correct_number:
#         attempts += 1
#         print(f"""Congradulations! {guess} was the correct number!
#         You guessed {attempts} times.""")
#         break
#     elif guess != correct_number:
#         if last_guess == 0: #Catches if the game is on its first turn still.
#             attempts += 1
#             last_guess = absolute_difference #saves the last absolute difference from the previous turn
#             print("Your guess was incorrect.")
#         elif absolute_difference == last_guess:
#             attempts += 1
#             last_guess = absolute_difference
#             print("Your guess was incorrect and was no closer than your last guess.")
#         elif absolute_difference < last_guess:
#             attempts += 1
#             last_guess = absolute_difference
#             print("Your guess was incorrect and was closer than your last guess.")
#         elif absolute_difference > last_guess:
#             attempts += 1
#             last_guess = absolute_difference
#             print("Your guess was incorrect and was further than your last guess.")

'''
To-do: Version 4
- import random
- allow the user to make a guess
- keep track of used guesses
- congradulate on win and make the user aware of the times attempted
- now with unlimited guess attempts
- tell user if they were closer to the correct answer
- get absolute difference between current and previous guess.
-Make the roles reversed, user gives number, computer tries to guess it.
'''

import random
import time

while True:
    correct_number = int(input("Please give a number from 1-10 for the computer to guess\n>"))
    if correct_number not in range(0,11):
        print("Your number was not within the range of 1-10, the computer will only guess within this range")
    else:
        break

attempts = 0
last_guess = 0
minimal = 0
maximum = 10
historic_guess = [0]
guess = 0

while True:
    while 0 in historic_guess: #Keeps computer from repeating same guesses
        guess = random.randint(minimal,maximum)
        if guess not in historic_guess:
            historic_guess += [guess]
            break
        elif guess in historic_guess:
            continue
    time.sleep(1)
    print(f"""Please guess a number between 1 and 10.
    > {guess}""")
    absolute_difference = abs(correct_number - guess) #Gives the absolute value of the difference between your guess and the correct number
    time.sleep(1)
    if guess not in range(1,11):
        print("Not a number between 1-10.")
    elif guess == correct_number:
        attempts += 1
        print(f"""Congradulations! {guess} was the correct number!
        You guessed {attempts} times.""")
        break
    elif guess != correct_number:
        if last_guess == 0: #Catches if the game is on its first turn still.
            attempts += 1
            last_guess = absolute_difference #saves the last absolute difference from the previous turn
            print("Your guess was incorrect.")

        elif absolute_difference == last_guess:
            attempts += 1
            last_guess = absolute_difference
            print("Your guess was incorrect and was no closer than your last guess.")

        elif absolute_difference < last_guess:
            attempts += 1
            last_guess = absolute_difference
            print("Your guess was incorrect and was closer than your last guess.")
            
        elif absolute_difference > last_guess:
            attempts += 1
            last_guess = absolute_difference
            print("Your guess was incorrect and was further than your last guess.")