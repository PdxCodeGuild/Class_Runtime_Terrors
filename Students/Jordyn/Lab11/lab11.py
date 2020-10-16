'''
To-do:
-list coin types
-ask for value amount
-define function to calculate coin count
-define function to calculate coin to coin value
-subtract coin to coin values from coint count
-print total in coin count values
'''

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

def coin_count(value, coin): #recieves tuple and calculates the number within the value
    coins = value // coin[1]
    # print(int(coins)) #testing output
    return int(coins)

def coin_subtract(value, coin_value): #subtracts the total coin value obtained from function coin_value, from the total value
    new_value = value - coin_value
    return int(new_value)

def coin_value(half_dollar, quarter, dime, nickel, penny): #returns the current coin value calculated
    half_dollar *= 50 #brings coin count to original full value
    quarter *= 25
    dime *= 10
    nickel *= 5
    coin_total = half_dollar + quarter + dime + nickel + penny
    # print(coin_total)
    return int(coin_total)

def play_again():
    yes_list = ["yes", "ya", "y"]
    no_list = ["no", "nah", "n"]
    while True:
        replay = input("Would you like to make more change? Y/N\n> ").lower()
        if replay in yes_list:
            return True
        elif replay in no_list:
            return False
        else:
            print("Sorry, that was not a supported option.")


print('Welcome to the Change Maker 5000 (tm)')

while True:
    half_dollar = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    value = float(input('Enter a dollar amount\n>$')) * 100
    # print(value)
    value = int(round(value))
    # print(value)

    i = 1
    for coin in coins:
        # print(coin)
        if i == 1: #calculates number of half-dollars within given value
            (half_dollar) = coin_count(value, coin)
            # print(half_dollar, 'half-dollars.')
            i += 1
        elif i == 2: #calculates quarters
            temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            quarter = coin_count(temp_value, coin)
            # print(quarter, 'quarters.')
            i += 1
            # break
        elif i == 3: #calculates dimes
            temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            dime = coin_count(temp_value, coin)
            # print(dime, 'dimes')
            i += 1
        elif i == 4: #calculates nickels
            temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            # print(temp_value)
            nickel = coin_count(temp_value, coin)
            # print(nickel, 'nickels')
            i += 1
        elif i == 5: #calculates pennies
            penny = value - coin_value(half_dollar, quarter, dime, nickel, penny)
            penny = int(round(penny))
            # print(value)
            # print(penny, 'pennies')
            i += 1
        else:
            break

    if half_dollar == 1: #section defines how the coin type is worded for propper grammar
        half_dollar = f' {half_dollar} half-dollar,'
    elif half_dollar == 0:
        half_dollar = ''
    else:
        half_dollar = f' {half_dollar} half-dollars,'

    if quarter == 1:
        quarter = f' {quarter} quarter,'
    elif quarter == 0:
        quarter = ''
    else:
        quarter = f' {quarter} quarters,'
    
    if dime == 1:
        dime = f' {dime} dime,'
    elif dime == 0:
        dime = ''
    else:
        dime = f' {dime} dimes,'

    if nickel == 1:
        nickel = f' {nickel} nickel,'
    elif nickel == 0:
        nickel = ''
    else:
        nicket = f' {nickel} nickels,'

    if penny == 1:
        penny = f' and {penny} penny.'
    elif penny == 0:
        penny = ' and 0 pennies.'
    else:
        penny = f' and {penny} pennies.'

    print(f'Your change is:{half_dollar}{quarter}{dime}{nickel}{penny}')

    again = play_again()
    if again == True:
        continue
    elif again == False:
        break
    else:
        print("This is the wrong way to break it")
        break