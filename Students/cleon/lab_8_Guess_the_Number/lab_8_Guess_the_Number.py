# cleon
#lab # 8 
import random

'''
# v_1

x = random.randint(1,10)
times = 0
while times < 10:
    guess =  int(input("Guess the number: "))
    if guess == x:
        print(f"correct! you guess {times + 1} times ")
        break
    else:
        if times == 9:
            print(" you lost! ")
            break
        else:
            times += 1
            print ("try again ")

'''
'''
#Version_ 2

x = random.randint(1,10)

times = 0
while True:
    guess =  int(input("Guess the number: "))
    if guess == x:
        print(f"correct! you guess {times + 1} times ")
        break
    else:
        times += 1
        print(f"Wrong! {times} guess so far ")
        continue



#Version_3

x = random.randint(1,10)
times = 0
while True:
    guess =  int(input("Guess the number: "))
    if guess == x:
        print(f"Correct! you guessed {times + 1} times ")
        break
    else:
        times += 1
        if guess > x:
            print(f" Too high! {times} guess so far")
            continue
        else:
            print(f" Too low! {times} guess so far")
            continue
        
'''
'''
#Version_4

def hot_or_cold(guess,x,past):
    if abs(x - past) >= abs(x - guess):
        print("colder")
    else:
        print("warm")

x = random.randint(1,10)
times = 0
while True:
    guess =  int(input("Guess the number: "))
    if guess == x:
        print(f"Correct! you guessed {times + 1} times ")
        break
    else:
        times += 1
        past = guess
        if times == 1:
            continue
        else:
            hot_or_cold(guess,x,past)
            continue
'''
#Version_5
x = random.randint(1,10)
times = 0
while True:
    guess =  int(input("Enter your number "))
    while True:
        x = random.randint(1,10)
        if x == guess:
            print("Correct!")
            break
        else:
            times += 1
            print(f"try again! You guessed {times} times ")
            continue
    break

            





    
    

