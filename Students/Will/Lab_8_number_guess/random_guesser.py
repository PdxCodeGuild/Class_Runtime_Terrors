import random

count = 0
attempts = 3
while count < attempts:
    count += 1
    x = random.randint(1,10)
    print (x)
    y = input("please guess a number between 0 and 10:   ")
    y = int(y)
    if x == y:
        print (f"correct! you guessed {count} times")
        break
    else: 
        if count < attempts:
            print("try again!")
        else:
            print ("sorry you loose")
            break    