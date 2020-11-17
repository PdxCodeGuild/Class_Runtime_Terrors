import string
import random
r = 'rock'
p = 'paper'
s = 'sissors'
def rps():
  print('Lets play Rock, Paper, Scissors!')
  while True:
    hand = input('Chose; type, rock, paper or sissors: \n ')
    if hand.lower() == r or hand.lower() == p or hand.lower() == s:
      win_conditions(hand)
      break
    else:
      print('please try again')
def win_conditions(hand):
  rps = ['rock','paper','sissors']
  cpu = random.choice(rps)
  player = hand
  print(f'Your choice was {hand}')
  if player == cpu:
    print(f'Game tied, {player} : {cpu}')
  elif player == 'rock' and cpu == 'paper':
    print(f'You lose {cpu} beats {player}')
  elif player == 'paper' and cpu == 'sissors':
    print(f'You lose {cpu} beats {player}')
  elif player == 'sissors' and cpu == 'rock':
    print(f'You lose {cpu}  eats {paper}')
  else:
    print(f'You win, {hand} beats {cpu}')
def rps_2():
  play_again = "" 
  print('Welcome to Rock Paper Scissors version 2! \n')
  print('Play as many times as you like. \n')
  while play_again != 'y' or play_again != 'n':
    rps()
    play_again = input('Like to play again? type y for yes or n for no: \n')
    if play_again.lower() == 'n':
      print('Goodbye')
      break
    elif play_again.lower() != 'y':
      print('enter valid input')

rps()      
rps_2()