import random
import string

#Constant Values
LETTERS = string.ascii_letters
PUNCTUATION = string.punctuation 
DIGITS = string.digits

#Emypt List
llist = []
plist= []
dlist = []

#User Input Fuction with Anti Number
def userinput(many):
    while True:
     x = input(f'\nHow many {many} do you want?\n\n')
     if (x.isdecimal()):
          x = int(x)    
          return (x)
     else:
          print('\nInvaid input try again!')


print("\n\nWelcome to the Password Generator")


x1 = userinput('Letter(s)')
x2 = userinput('Character(s)')
x3 = userinput('Number(s)')

# For Loops with Anti Zero Break   
if x1 != 0:
     for loop1 in range(x1):
          llist.append(random.choice(LETTERS))
if x2 != 0:
     for loop2 in range(x2):
          plist.append(random.choice(PUNCTUATION))
if x3 != 0:
     for loop3 in range(x3):
          dlist.append(random.choice(DIGITS))

list = llist + plist + dlist #One List
random.shuffle(list) #Shuffle List
joinlist = ''.join(list) # Join List
xT= x1 + x2 + x3

print(f'\n\nYour {xT} length password with {x1} Letters, {x2} Characters, and {x3} Numbers is',joinlist,'\n\n')

