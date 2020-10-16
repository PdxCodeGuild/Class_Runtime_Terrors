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
    while guess != x and guesscount != 10:
        if guess != x:
            guesscount += 1
            guess =  userinput()
            if guess != x:
                print('Try again')
    if guesscount == 10 and guess != x:
        print("You have lost. You have Failed 10 Guesses")
    else:
        print(f'Correct! You guessed {guesscount} time(s)')

x = random.randint(1,10)


# print("This is debuging Code the number is ",x)  #Use Comments to add the debuging code tool 
print("Welcome to the guess the Number Game")
main()

