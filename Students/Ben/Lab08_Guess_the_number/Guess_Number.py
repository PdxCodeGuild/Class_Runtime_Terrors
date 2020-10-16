# 10/15/2020
# Random.randint; 
#####################################################
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
import random
x = random.randint(1,10)
guess = 0

while guess != x:
    guess = int(input("Guess the number: "))
    if guess == x:
        print("Correct")
        break
    elif guess > x:
        print("Too high!")
    else:
        print("Too low!")
####################################################
# Version 4
import random
x = random.randint(1,10)
print(x)
