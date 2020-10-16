import random

def userinput():
    while True:
     x = input('Guess the number: ')
     try:
          x = int(x)    
          return (x)
     except:
          print('\nInvaid input try again!')

def main():
    guesscount = 0
    guess = 0
    while True:
        if guess != x:
            guesscount += 1
            guess =  userinput()
            if guess != x:
                if guess > x:
                    print('Too high!')
                else:
                    print('Too low!')
            else:
                break
  
    print(f'Correct! You guessed {guesscount} time(s)')

x = random.randint(1,10)


print("This is debuging Code the number is ",x)  #Use Comments to add the debuging code tool 
print("Welcome to the guess the Number Game")
main()

