import random

def pick6():
    the6 = []
    while len(the6) < 6:
        the6.append(random.randint(0,99))
    return the6

both_lists = (pick6(),pick6())
(pick6 , win6) = both_lists

for x in range(len(pick6)):
    wins = 0
    if pick6[x] == win6[x]:
        wins += 1
    else:
        continue

try: 
    print(pick6)
    print(win6)
    print(f"number of wins is {wins}")    

finally: 
    print("the application has run")


# create list

