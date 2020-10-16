import random

user_choice = input ('Rock, paper, scissors? ').lower()
print(f'you chose {user_choice}')
computer_choice = random.randint(1,3)
#print (computer_choice)

def get_computer():
  global computer_choice
  #computer_choice = random.randint(1,3)
  if computer_choice == 1:
      print ('computer chooses rock') 
      computer_choice = 'Rock'
      compete()
      return computer_choice
  elif computer_choice == 2:
      print ('computer choses paper')
      computer_choice = 'Paper'
      compete()
      return computer_choice
  elif computer_choice == 3:
      print ('computer choses scissors')
      computer_choice = 'Scissors'
      compete()
      return computer_choice
  
def compete ():
  if computer_choice =='Rock' and user_choice == 'rock':
    print ('its a tie')
  elif computer_choice =='Rock' and user_choice == 'paper':
    print ('paper beats rock, user wins')
  elif computer_choice =='Rock' and user_choice == 'scissors':
    print ('paper beats rock, computer wins')
  elif computer_choice =='Scissors' and user_choice == 'scissors':
    print ('its a tie')
  elif computer_choice =='Scissors' and user_choice == 'rock':
    print ('rock beats scissors, user wins')
  elif computer_choice =='Scissors' and user_choice == 'paper':
    print ('scissors beats paper, computer wins')
  elif computer_choice =='Paper' and user_choice == 'paper':
    print ('its a tie')
  elif computer_choice =='Paper' and user_choice == 'scissors':
    print ('scissors beats paper, user wins')
  elif computer_choice =='Paper' and user_choice == 'rock':
    print ('papers beats rock, computer wins')
  else:
    print ('error')

get_computer()
    