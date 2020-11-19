# 10/15/2020
# Random.randint; 
####################################################
# Version 1
# import random
# x = random.randint(1,10)
# i = 1

# while i <= 10:
#     guess = int(input("Guess the number: "))
#     if guess == x:
#         print(f"Correct! You guessed {i} times")
#         break
#     else:
#         print("try again!")
#     i += 1
# else:
#     print("You Lost") 
####################################################
# Version 2
# import random
# x = random.randint(1,10)
# a = False
# i = 1

# while a is False:
#     guess = int(input("Guess the number: "))
#     if guess == x:
#         print(f"Correct! You guessed {i} times")
#         a = True
#     else:
#         i += 1
#         print("try again!")
####################################################
# Version 3
# import random
# x = random.randint(1,10)
# guess = 0

# while guess != x:
#     guess = int(input("Guess the number: "))
#     if guess == x:
#         print("Correct")
#         break
#     elif guess > x:
#         print("Too high!")
#     else:
#         print("Too low!")
####################################################
# # Version 4
# import random
# x = random.randint(1,10)
# print(x)
# guess = 0
# attempt = 1

# while guess != x:
#     guess = int(input("Guess the number: "))
#     if guess == x:
#         print("Correct")
#         break
#     else: 
#         if attempt == 1:
#             print('This is your first attemp, no hisotrical comparison available')
#             attempt += 1
#             last_guess = guess 
#         else:
#             print(f'your last guess is {last_guess}')
#             diff_now = abs(guess-x)
#             diff_prev = abs(last_guess-x)
#             if diff_now < diff_prev:
#                 print("You are closer now")
#             else:
#                 print("you are further now than your last guess")
#     last_guess = guess 
############################################################
# Version 5
import random
answer = int(input("Please enter the number you would like computer to guess: "))
guess = False
while guess is False:
    computer = random.randint(0,1000)
    if computer == answer:
        print(f"computer have successfully guessed your number which is {computer}")
        guess = True
    else:
        print("Computer failed in the last guess, guessing a new number now")

        