


import random



# version 1 implementation 1

# computer_choice = random.randint(1,10)
# i = 0
# while i < 10:
#     user_guess = int(input('guess a number: '))
#     if user_guess == computer_choice:
#         print('you won!')
#         break
#     i += 1
# else:
#     print('you lost')

# version 1 implementation 2

# computer_choice = random.randint(1,10)
# for i in range(1, 11):
#     user_guess = int(input(f'{i} guess a number: '))
#     if user_guess == computer_choice:
#         print(f'you won! it took {i} guesses')
#         break
# else:
#     print('you lost')

# version 1 implementation 3

# computer_choice = random.randint(1,10)
# num_guesses = 1
# while True:
#     user_guess = int(input('guess a number: '))
#     if user_guess == computer_choice:
#         print('you won!')
#         exit()
#     if num_guesses == 10:
#         print('you lost!')
#         exit()
#     num_guesses += 1


# version 2

# computer_choice = random.randint(1,10)
# num_guesses = 0
# while True:
#     user_guess = int(input('guess a number: '))
#     num_guesses += 1
#     if user_guess == computer_choice:
#         print(f'You won! It took {num_guesses} guesses')
#         break


# version 3

# computer_choice = random.randint(1,10)
# num_guesses = 0
# while True:
#     user_guess = int(input('guess a number: '))
#     num_guesses += 1
#     if user_guess == computer_choice:
#         print(f'You won! It took {num_guesses} guesses')
#         break
#     if user_guess < computer_choice:
#         print('Too low!')
#     # elif user_guess > computer_choice
#     else:
#         print('Too high!')


# version 4

# computer_choice = random.randint(1,10)
# print(computer_choice)
# num_guesses = 0
# previous_guess = None
# while True:
#     user_guess = int(input('guess a number: '))
#     num_guesses += 1
#     if user_guess == computer_choice:
#         print(f'You won! It took {num_guesses} guesses')
#         break

#     # version 3
#     if user_guess < computer_choice:
#         print('Too low!')
#     else:
#         print('Too high!')

#     # version 4
#     if previous_guess is not None:
#         distance_current = abs(user_guess-computer_choice)
#         distance_previous = abs(previous_guess-computer_choice)
#         if distance_current < distance_previous:
#             print('Warmer!')
#         elif distance_current > distance_previous:
#             print('Colder!')
#         else:
#             print('Same temperature!')
    
#     previous_guess = user_guess
    


# i = 1
# while i <= 10:
#     correct = input(f'Is your number {i}?')
#     if correct == 'yes':
#         print('I win!')
#         break
#     i += 1


# low = 1
# high = 100
# guesses = 0
# while True:
#     if high-low <= 1:
#         mid = high
#     else:
#         mid = (low + high) // 2
#     print(low, high)
#     guesses += 1
#     correct = input(f'Is your number {mid}?')
#     if correct == 'yes':
#         print('I win!')
#         print(f'That took {guesses} guesses')
#         break
#     higher_lower = input(f'Is your number higher or lower than {mid}?')
#     if higher_lower == 'higher':
#         low = mid
#     else:
#         high = mid
    
