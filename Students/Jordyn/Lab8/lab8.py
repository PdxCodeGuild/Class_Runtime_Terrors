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
'''

import random

correct_number = random.randint(1,10)

attempts = 0
last_guess = 0

while True:
    guess = int(input('Guess a number from 1 to 10!\n> '))
    if guess not in range(1,11):
        print("Not a number between 1-10.")
    elif guess == correct_number:
        attempts += 1
        print(f"Congradulations! {guess} was the correct number!\n You guessed {attempts} times.")
        break
    elif guess != correct_number:
        attempts += 1
        
        if guess 