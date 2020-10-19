import random
rand_num = random.randint (1,10)

def main():
    
    guess = int(input('You have 10 attempts to guess a number between 1 and 10: '))
    attempts = 1
    while attempts < 10:
          if guess != rand_num:
            guess = int(input('Wrong, Guess again: '))
            attempts += 1 
          else:
          
            print('Correct! You guessed the number in', attempts , 'attempts..')
            break
    print('You used up all of your tries, better luck nest time.')

main()
