import random


game = ['Rock', 'Paper', 'Scissors']
R = "Rock"
P = "Paper"
S = 'Scissors'

def userinput():
    while True:
     uinput = input('\nRock, Paper or Scissors?\n').title()
     if ((uinput == R) or (uinput == P) or (uinput == S)):    
          return (uinput)
     else:
          print('\nInvaid input try again!')

def again():
    while True:
        again = input('Enter \'y\' to try again, \'n\' to quit: ').lower()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print('Only \'y\' or \'n\' inputs are vaild')


def main():
    while True:
        user = userinput()
        comp = random.choice(game)

        if user == comp:
            message = ('Tie')
        elif ((user == R)and(comp == S)) or ((user == P)and(comp == R)) or ((user == S)and(comp == P)):
            message = ('Win')
        else:
            message = ('Lose')
        
        print(f'\n\nYou Picked {user}, The Computer Picked {comp}, You {message}!')
        if again() == False:
            break

print('Welcome to the rock, paper, scissors game')

main()

print('\n\nThanks for playing Goodbye!\n\n')
