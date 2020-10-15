#version 1 
import random 

new = []
available_characters = 'a123456789AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
#available_characters = a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
available_characters = list(available_characters)
#available_characters = random.shuffle(available_characters)
#print (available_characters)
password_length = 8 
i = 0

while i < 8:
  i+=1
  choice = random.choice(available_characters)
  new.append(choice)
  #print (choice)

new = ''.join(new)
print (new)

#version 2
import random 

new = []
available_characters = 'a123456789AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
#available_characters = a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
available_characters = list(available_characters)
#available_characters = random.shuffle(available_characters)
#print (available_characters)
password_length = int(input('how long would you like your password? '))
i = 0

while i < password_length:
  i+=1
  choice = random.choice(available_characters)
  new.append(choice)
  #print (choice)

new = ''.join(new)
print (new)

#version 2



