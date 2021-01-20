#version 1
import random 

x = random.randint(1,10)
#print (x)
#user_input = int (input ('guess that number: '))
guesses = 0 

while guesses < 10:
    user_input = int (input ('guess that number: '))
    if user_input == x:
        print ('nailed it')
        break
    else:
        guesses+=1
        print ('guess again')
        continue 
print ('Your out of guesses')

# version 2 
x = random.randint(1,10)
#print (x)
#user_input = int (input ('guess that number: '))
guesses = 0 

while True:
    user_input = int (input ('guess that number: '))
    if user_input == x:
        print ('nailed it')
        break
    else:
        guesses+=1
        print (f'guess again. You guessed {guesses} times')
        continue 
#print ('Your out of guesses')

#version 3 
x = random.randint(1,10)
#print (x)
#user_input = int (input ('guess that number: '))
guesses = 0 

while True:
    user_input = int (input ('guess that number: '))
    if user_input == x:
        print ('nailed it')
        break
    elif user_input < x:
        guesses+=1
        print (f'guess again. You guessed too low. You guessed {guesses} times')
        continue 
    elif user_input > x:
        guesses+=1
        print (f'guess again. You guessed too high. You guessed {guesses} times')
        continue 