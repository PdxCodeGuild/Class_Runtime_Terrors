import random

def userinput():
    while True:
     x = input('Give the computer a number to guess: ')
     try:
          x = int(x)    
          return (x)
     except:
          print('\nInvaid input try again!')

def main():
    guesscount = 0
    guess = 0
    userx = userinput()
    x= 0 # First Time
    while True:
        if userx != x:
            guesscount += 1
            x = random.randint(1,10)
            if guess != x:
                print('The Computer Guessed ',x)
        else:
            break
  
    print(f'It took the computer {guesscount} time(s)')

print("The compueter will guess your number")
main()

