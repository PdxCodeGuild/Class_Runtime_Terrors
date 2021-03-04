

import random
numbers = ['0','1','2','3','4','5','6','7','8','9']

pass_len = int(input('How long would you like your password to be?: ')) 
n = 0
pick = str()
while n < pass_len:
    pick = pick + random.choice(numbers)  
    n += 1
        
print(pick)


