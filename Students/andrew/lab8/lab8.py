"""GUESS THE NUMBER"""
import random
import time

def guess_v1():
    count = 10
    guess = 0
    num = random.randint(1, 10)
    print("Try to guess a number between between 1 and 10. \n You have 10 tries!")
    
    while count > 0 and num != int(guess):
        guess = input("Enter a guess: \n")
        count -= 1
        if num == int(guess):
            print(f'Great job! You guessed the right number: {num} \n')
        else:
            print(f'Sorry, {guess} is not the correct number.')


def guess_v2():
    count = 0
    guess = 0
    num = random.randint(1, 10)
    print("Try to guess a number between between 1 and 10. \n ")
    
    while num != int(guess):
        guess = input("Enter a guess: \n")
        count += 1
        if num == int(guess):
            print(f'Great job! You guessed the right number: {num} \n It took you {count} tries.')
        else:
            print(f'Sorry, {guess} is not the correct number.')


def guess_v3():
    count = 0
    guess = 0
    num = random.randint(1, 10)
    print("Try to guess a number between between 1 and 10. \n ")
    
    while num != int(guess):
        guess = input("Enter a guess: \n")
        count += 1
        if num == int(guess):
            print(f'Great job! You guessed the right number: {num} \n It took you {count} tries.')
        elif int(guess) < num:
            print("Your a bit low...\n")
        elif int(guess) > num:
            print("You're too high.")



def guess_v4():
    count = 0
    guess = 0
    guessed_num = 0
    num = random.randint(1, 10)
    print("Try to guess a number between between 1 and 10. \n ")
    
    while num != int(guess):
        guess = input("Enter a guess: \n")
        count += 1
        last_guess = guessed_num
        guessed_num = 0
        
        #print(guessed_num)

        if num == int(guess):
            print(f'Great job! You guessed the right number: {num} \n It took you {count} tries.')
            break
        while num != int(guess):
            if num == int(guess):
                print(f'Great job! You guessed the right number: {num} \n It took you {count} tries.')

            elif int(guess) < num:
                print("Your a bit low...\n")
                guessed_num = int(guess)

                if guessed_num != 0:
                    compare(last_guess, guessed_num)
                    break
            elif int(guess) > num:
                print("You're too high.")
                guessed_num = int(guess)
                if guessed_num != 0:
                    compare(last_guess, guessed_num)
                    break
            

def compare(x , y):
    target = x
    guessed_num = y
    #print(x,y)
    if target > guessed_num:
        print("Thats lower than last time")
    elif target < guessed_num:
        print("Thats higher than last time")
    elif target == guessed_num:
        print("Both are same")


        
        

def guess_v5():
    guess = 0
    count = 10
    num = random.randint(1, 10)
    print(" The CPU will try to guess a number between between 1 and 10. \n Lets see if it can do it in less than 10 tries!")
    
    while count > 0 and num != int(guess):
        guess = random.randint(1,10)
        count -= 1
        if num == int(guess):
            print(f'Awesome! The CPU guessed the right number: {num} \n')
        else:
            print(f'Sorry, {guess} is not the correct number.')
            print("Thinking")
            time.sleep(.5)
            print(".")
            time.sleep(.5)
            print(".")
            time.sleep(.5)
    print('The CPU ran out of tries!')

""" RUN FUNCTIONS HERE"""
guess_v1()
guess_v5()   
        




