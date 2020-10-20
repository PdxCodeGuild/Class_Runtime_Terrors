# TODO Fix output at the end of money conversion
# TODO Refactor code to help readability


def money_handler():
    correct_input = False
    while correct_input == False:
        try:
            money = float(input("please enter a dollar amount:"))
            if money < 0.01:
                print("That is not enough money to convert! \n")
            else:
                return money
                # break
        except:
            print("Please enter numbers in a x.xx format, ie. 1.23: \n")


def continue_conversion(stop):
    cont = False
    while cont == False:
        try:
            convert_again = input(
                "Would you like to convert more money? n for no or y for yes: \n")
            if convert_again.lower() == 'y':
                money = money_handler()
                convert(money)

            if convert_again.lower() == 'n':
                stop = True
                return stop
        except Exception as e:
            print(e)

        else:
            print(
                f'{convert_again} is not a valid input! Please enter y or n to continue or close.\n')


def convert(dollars):
    hdcount = 0         # Variables keeping track of coin count
    qcount = 0
    dcount = 0
    ncount = 0
    money = float(dollars)

    if money // .50:        # If statements check value of money to see if it is divisible by coins value
        hdcount = money // .50
        money = money - (hdcount * .5)
        money = round(money, 3)

    if money // .25:
        qcount = money // .25
        money = money - (qcount * .25)
        money = round(money, 3)

    if money // .10:
        dcount = money // .10
        money = money - (dcount * .10)
        money = round(money, 3)

    if money // .05:
        ncount = money // .05
        money = money - (ncount * .05)
        money = round(money, 3)

    # Pennies are the remainder of the preceeding operations, multiplying by 100 gives us the correct amout
    pennies = money * 100
    formatted = '{:.0f}'.format(pennies)

    print(
        f'You have: \n {hdcount}:Hlaf-Dollars \n {qcount}: Quarters \n {dcount}: Dimes \n {ncount}: nickles \n {formatted}: pennies ')

# change maker calls conver function and passes in dollar as a argument


def change_maker_5000():
    stop = False
    print("Welcome to the change maker \n")
    while stop == False:
        dollar = money_handler()
        convert(dollar)
        stop = continue_conversion(stop)


def main():
    change_maker_5000()


main()
