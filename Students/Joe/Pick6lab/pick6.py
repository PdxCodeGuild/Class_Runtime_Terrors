import random 

def function (instance):
  bracket = [] #Storage of user and lottery ticket
  if instance == 'user':
    for number in range(0,6):
      user_ticket = random.randint(1,100)#random number saved in variable 
      bracket.append(user_ticket)#appended that random number to the  bracket 
  elif instance == 'actual':
    for number in range(0,6): 
      actual = random.randint(1,100)#random number saved in variable
      bracket.append(actual)#appended that random number to the bracket
  return bracket

def compare (user_ticketing, actual_ticketing):
  score = 0 
  coin = 0 
  for x in range (len(user_ticketing)):
    if user_ticketing[x] == actual_ticketing[x]:
      score = score + 1 
  if score == 1:
      coin += 4
  if score == 2:
      coin += 7
  if score == 3:
      coin += 100
  if score == 4:
      coin += 50000
  if score == 5:
      coin += 1000000
  if score == 6:
      coin += 25000000
  return coin 

def main ():
  spent = 0
  wins = 0
  user_ticketing = function ('user')
  for num in range (0,1000): 
    spent += 2
    actual_ticketing = function ('actual')
    score_report = compare (user_ticketing, actual_ticketing)
    wins = wins + score_report
  print (f'You spent ${spent}')
  print (f'You won ${wins}')
  print(f" ROI: {(wins - spent) / spent}" )
main ()
