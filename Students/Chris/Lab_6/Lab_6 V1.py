
import random 

new = []
available_characters = 'AabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

available_characters = list(available_characters)
#available_characters = random.shuffle(available_characters)

password_length = 10
l = 0

while l < 10:
  l=l+1
  choice = random.choice(available_characters)
  new.append(choice)
  

new = ''.join(new)
print (new)
