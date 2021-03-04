# program to make change
# 10/16/2020
# Tom Schroeder

play_again = True # initialize variable foor while loop to continue program until user quits

# list of tuples with currency values, divided values in lab by 100 
coins = [
    ('quarter', .25),
    ('dime', .10),
    ('nickel', .05),
    ('penny', .01)
    ]

while play_again:
     
    # user enters currency amount
    money_amount = input ('Enter the amount amount of money to convert to change: \n')
    

    float_convert = False # initializes variable to False for loop that checks entry is a float
    while float_convert == False: # loops until user enters a float
        try:
            money_amount = float(money_amount)
            float_convert = True
        
        except ValueError:
            money_amount = input ('Your entry is not a valid entry. Enter the amount amount of money to convert to change: \n')

    # converts input string to a float
    money_amount = float(money_amount)

    # performs floor division to calculate number of quarters
    number_quarters = money_amount // coins[0][1]
    # print (f'{number_quarters} quartes')

    # determines remaining value after quarters accounted for
    money_amount_less_quarters = round(money_amount % coins[0][1], 2)
    # print (f'{money_amount_less_quarters} money_amount_less_quarters')

    # performs floor division to calculate number of dimes
    number_dimes = money_amount_less_quarters // coins[1][1]
    # print (f'{number_dimes} dimes')

    # determines remaining value after dimes accounted for
    money_amount_less_dimes = round(money_amount_less_quarters % coins[1][1], 2)
    # print (f'{money_amount_less_dimes} money_amount_less_dimes')

    # performs floor division to calculate number of nickels
    number_nickels = money_amount_less_dimes // coins[2][1]
    # print (f'{number_nickels} nickels')

    # determines remaining value after nickels accounted for
    money_amount_less_nickels = round(money_amount_less_dimes % coins[2][1], 2)
    # print (f'{money_amount_less_nickels} money_amount_less_nickels')

    # performs division to calculate number of pennies
    number_pennies = money_amount_less_nickels / coins[3][1]

    # converts all coin quanties to intergers
    number_quarters = int(number_quarters)
    number_dimes = int(number_dimes)
    number_nickels = int(number_nickels)
    number_pennies = int(number_pennies)
    
    # prints user's inputed amount and the number of coins
    print(f'${money_amount} is made up of {number_quarters} quarters, {number_dimes} dimes, {number_nickels} nickels, {number_pennies} pennies.')

    # asks user if they want to repeat the program or quit. loops until user gives valid answer 
    play_again_input = input ('Would you like to do another one? "Y" or "N"').capitalize()
    while play_again_input != 'Y' and play_again_input != 'N':
        play_again_input = input ('You made an incorrect entry. Would you like to do another one? "Y" or "N"').capitalize()
    
    if play_again_input == 'Y':
        play_again = True
    
    elif play_again_input == 'N':
        play_again = False