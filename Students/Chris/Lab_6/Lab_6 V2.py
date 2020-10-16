

import random 

new = []
available_characters = 'AabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

available_characters = list(available_characters)

password_length = int(input('how long would you like your password? '))
l = 0

while l < password_length:
  l=l+1
  choice = random.choice(available_characters)
  new.append(choice)
  #print (choice)

new = ''.join(new)
print (new)