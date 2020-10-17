# program to make change
# 10/16/2020
# Tom Schroeder

play_again = True

while play_again:
        
    money_amount = input ('Enter the amount amount of money to convert to change: \n')
    
    float_convert = False
    while float_convert == False:
        try:
            money_amount = float(money_amount)
            float_convert = True
        
        except ValueError:
            money_amount = input ('Your entry is not a valid entry. Enter the amount amount of money to convert to change: \n')

    quarters                   = money_amount // .25
    # print (f'{quarters} quartes')

    money_amount_less_quarters = round(money_amount % .25, 2)
    # print (f'{money_amount_less_quarters} money_amount_less_quarters')

    dimes                      = money_amount_less_quarters // .1
    # print (f'{dimes} dimes')

    money_amount_less_dimes    = round(money_amount_less_quarters % .1, 2)
    # print (f'{money_amount_less_dimes} money_amount_less_dimes')

    nickles                   = money_amount_less_dimes // .05
    # print (f'{nickles} nickles')

    money_amount_less_nickles  = round(money_amount_less_dimes % .05, 2)
    # print (f'{money_amount_less_nickles} money_amount_less_nickles')

    pennies = money_amount_less_nickles / .01

    quarters = int(quarters)
    dimes = int(dimes)
    nickles = int(nickles)
    pennies = int(pennies)
    
    print(f'${money_amount} is made up of {quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies.')

    
    play_again_input = input ('Would you like to do another one? "Y" or "N"').capitalize()
    while play_again_input != 'Y' and play_again_input != 'N':
        play_again_input = input ('You made an incorrect entry. Would you like to do another one? "Y" or "N"').capitalize()
    
    if play_again_input == 'Y':
        play_again = True
    
    elif play_again_input == 'N':
        play_again = False