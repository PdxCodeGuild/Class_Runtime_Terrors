



import math

def round_pad_zeroes(num, digits=2):
    num = str(float(round(num, digits)))
    num += '0'*(digits-len(num)+1+num.index('.'))
    return num

# print(round_pad_zeroes(5, 3)) # 5.000
# print(round_pad_zeroes(3.1415963, 3)) # 3.142
# print(round_pad_zeroes(3.1, 5)) # 3.10000



def get_plural(value, single_string, plural_string):
    return single_string if value == 1 else plural_string

def make_change_v1(dollars):
    
    pennies = dollars*100
    pennies = round(pennies)

    # print(pennies/25)
    # print(math.floor(pennies/25))
    # print(int(pennies/25))

    quarters = pennies//25
    pennies -= quarters*25 # pennies %= 25
    dimes = pennies//10
    pennies -= dimes*10
    nickels = pennies//5
    pennies -= nickels*5

    if quarters > 0:
        if quarters > 1:
            print(quarters, 'quarters', end=', ')
        else:
            print(quarters, 'quarter', end=', ')
    if dimes > 0:
        print(dimes, 'dime' if dimes == 1 else 'dimes', end=', ')
    if nickels > 0:
        print(nickels, get_plural(nickels, 'nickel', 'nickels'), end=', ')
    if pennies > 0:
        print(pennies, 'pennies')

# dollars = input('what is the dollar amount? $') # 0.87
# dollars = float(dollars)
# make_change_v1(dollars)

def make_change_v2(dollars, coins):
    pennies = dollars*100
    pennies = round(pennies)
    output = []
    for coin in coins:
        coin_count = pennies//coin[2]
        pennies -= coin_count*coin[2]
        if coin_count > 0:
            output.append(str(coin_count) + ' ' + get_plural(coin_count, coin[0], coin[1]))
            #output.append(f'{coin_count} {coin[1]}')
    print(', '.join(output))
        

coin_values = [
    ('half-dollar', 'half-dollars', 50),
    ('quarter', 'quarters', 25),
    ('dime', 'dimes', 10),
    ('nickel', 'nickels', 5),
    ('penny', 'pennies', 1)
]
while True:
    dollars = input('what is the dollar amount? $') # 0.87
    dollars = float(dollars)
    print('making change for $' + round_pad_zeroes(dollars))
    make_change_v2(dollars, coin_values)
    keep_going = input('would you like to make change again? y/n ').lower().strip()
    if keep_going == 'n':
        break


