import random

count = 0

while True:
    count += 1
    x = random.randint(1,10)
    print (f"count = {count}")
    print (f"random = {x}")
    y = input("please guess a number between 0 and 10:   ")
    y = int(y)
    if x == y:
        if count == 1:
            print ("correct you only guessed once")
        else:    
            print (f"correct! you guessed {count} times")
        break
    elif y>x:        
        print(f"your guess is high, try again!")
    elif y<x:
        print("your guess is low, try again!")

    