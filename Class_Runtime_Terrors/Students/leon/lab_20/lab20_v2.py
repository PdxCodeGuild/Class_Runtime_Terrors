# PDX Fullstack lab 20 version 2
# Pick Six
# ROI computation included

from random import randint

ticket = [0,0,0,0,0,0]
win = 0

# generate a list of 6 ramdon digits
def pick6(ticket):  
    ticket = [0,0,0,0,0,0]  
    i = 0
    while (i < 6):
        ticket[i] = (randint(1,99))
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
    earnings = 0       
    expense = 0
    # iteration variable; loop 100,000 times              
    n = 100000
    # intro blurb
    print("Welcome to Pick 6!")
    print("Tickets cost $2")
    # primary loop
    while n > 0:
        # reset tickets
        expense += 2
        WinTick = [0,0,0,0,0,0] 
        PlayTick = [0,0,0,0,0,0]
        WinTick = pick6(ticket)
        PlayTick = pick6(ticket)
        win = num_matches(WinTick, PlayTick)
        if win > 0:
            if win > 5:
                earnings = earnings + 25000000
                win = 0
            elif win > 4:
                earnings = earnings + 1000000
                win = 0
            elif win > 3:
                earnings = earnings + 50000
                win = 0
            elif win > 2:
                earnings = earnings + 100
                win = 0
            elif win > 1:
                earnings = earnings + 7
                win = 0
            elif win > 0:
                earnings = earnings + 4
                win = 0
            else:
                win = 0
        n = n -1

    balance = earnings - expense
    print("Your final balance is: ", balance)
    roi = balance / expense
    print("Your ROI is: ", roi)

main()