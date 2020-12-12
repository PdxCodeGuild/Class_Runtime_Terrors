import random

balance = 100000
def play():
    def pick6():
        the6 = []
        while len(the6) < 6:
            the6.append(random.randint(0,99))
        return the6
    both_lists = (pick6(),pick6())
    (pick_list , win_list) = both_lists
    print(pick_list)
    print(win_list)
    for x in range(len(pick_list)):
        wins = 0
        if pick_list[x] == win_list[x]:
            wins += 1
        else:
            continue
    print(wins)
    return wins
def multiple_plays(x,balance):
    counter = 0
    while counter < x:
        balance -= 2
        play()
        counter += 1  
    print(balance)   
    return balance
def qty_play():
    x = input( "enter the number of times you would like to play: ")
    x = int(x)
    return x
multiple_plays(qty_play(), balance)
    