"""
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:
"""

import random

def guessTheNumber():
    count = 0
    ran_num = random.randint(1,10)
    while count < 10:
        count =+ 1
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == ran_num:
            print("You won")
            break
        else:
            print("try again!")


def guessTheNumberV2():
    count = 0
    won = False
    ran_num = random.randint(1,10)
    while not won:
        count = count + 1
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == ran_num:
            print("You won after ", count, " tries")
            won = True
        else:
            print("try again!")
            
def guessTheNumberV3():
    count = 0
    won = False
    ran_num = random.randint(1,10)
    while not won:
        count = count + 1
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == ran_num:
            print("You won after ", count, " tries")
            won = True
        elif guess > ran_num:
            print("try again, too high")
        else:
            print("try again, too low")
        

def main():
    guessTheNumberV3()

if __name__ == '__main__':
    main()


