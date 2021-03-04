
import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
n = 0
pick = str()
while n < (10):
    pick = pick + random.choice(numbers)    
    n += 1

print(pick)
