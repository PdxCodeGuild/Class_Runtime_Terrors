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
    guess = 0 # Guess Var
    guessc = 0# Guess Check Var
    lguess = 0# Last Guess Var
    while True:
        if guess != x:
            guesscount += 1
            guess =  userinput()
            if guess != x:
                if guesscount != 1: #Skiping the first abs check
                    guessc = abs(x- guess) # Abs of Guess
                    if guessc > lguess: # Comparing the last guess to new guess
                        print('Colder')
                        lguess = guessc
                    else:
                        print('Hotter')
                        lguess = guessc
                else: #Only Run the first time
                    if guess > x:
                        print('Too high!')
                        lguess = abs(x-guess)
                    else:
                        print('Too low!')
                        lguess = abs(x-guess)
            else:
                break
  
    print(f'Correct! You guessed {guesscount} time(s)')

x = random.randint(1,10)


print("This is debuging Code the number is ",x)  #Use Comments to add the debuging code tool 
print("Welcome to the guess the Number Game")
main()

