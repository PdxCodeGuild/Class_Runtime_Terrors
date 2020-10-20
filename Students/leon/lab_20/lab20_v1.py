# PDX Fullstack lab 20 version 1
# Pick Six
import random

ticket = [0,0,0,0,0,0]
win = 0

# generate a list of 6 ramdon digits
def pick6(ticket):  
    ticket = [0,0,0,0,0,0]  
    i = 0
    while (i < 6):
        ticket[i] = (random.randint(1,99))
        i += 1
    return(ticket)

# compares Player to Computer ticket
# returning number of matches; winning = WinTick; tick = PlayTick
def num_matches(winning, tick):   
    j = 0        
    win = 0               
    while j < 6:
        if (winning[j] == tick[j]):
            win += 1
        
        j += 1
    return(win)

def main():
    # starting balance
    balance = 0       
    # iteration variable; loop 100,000 times              
    n = 100000
    # intro blurb
    print("Welcome to Pick 6!")
    print("Tickets cost $2")
    # primary loop
    while n > 0:
        # reset tickets
        WinTick = [0,0,0,0,0,0] 
        PlayTick = [0,0,0,0,0,0]
        WinTick = pick6(ticket)
        PlayTick = pick6(ticket)
        win = num_matches(WinTick, PlayTick)
        if win > 0:
            if win > 5:
                balance = balance + 25000000
                win = 0
            elif win > 4:
                balance = balance + 1000000
                win = 0
            elif win > 3:
                balance = balance + 50000
                win = 0
            elif win > 2:
                balance = balance + 100
                win = 0
            elif win > 1:
                balance = balance + 7
                win = 0
            elif balance > 0:
                balance = balance + 4
                win = 0
            else:
                win = 0
        n = n -1

    
    print("Your final balance is: ", balance)


main()