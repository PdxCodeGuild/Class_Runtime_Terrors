import random

def play():
    balance = 0
    wins_reward = {1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
    counter = 0
    x = input( "enter the number of time you would like to play: ")
    x = int(x)
    while counter < x:
        balance -= 2
        counter += 1
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
            print(wins)
            print(balance)

    return print(f"the the number of wins is {wins} and balance is {balance}")

play()
print("the application has run")


# create list

