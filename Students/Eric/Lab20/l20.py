import random

def pick6(): # Pick 6 Fuctions Returns a List of 6
    pick = []
    for x in range(6):
        pick.append(random.randint(1, 99))
    return pick

def num_matches(win6, loser6): #Check for matches Fuctions, Returns Numbers of Matches
    match  = 0
    for x in range(5): 
        if loser6[x] == win6[x]:
            match +=1
    return match

def winning(matchreturn): # Money won Fuctions, Return Winning in Value
    if matchreturn == 1:
        return 4
    if matchreturn == 2:
        return 7
    if matchreturn == 3:
        return 100
    if matchreturn == 4:
        return 50000
    if matchreturn == 5:
        return 1000000
    if matchreturn == 6:
        return 25000000
    else:
        return 0

def main():
    startmoney = 0
    winmoney = 0
    win6 = pick6()
    for x in range(100000):
        startmoney +=2 
        loser6 = pick6()
        matchreturn= num_matches(win6, loser6)
        winmoney += winning(matchreturn)

    print("You just bought 100,000 Tickets at 2 bucks each!")  
    print("You spent: ",startmoney)
    print("You won: ",winmoney)
    print("For a ROI of: ",((winmoney - startmoney)/startmoney)*100,"%")


print("Welcome to the Pick6 Lab")
main()