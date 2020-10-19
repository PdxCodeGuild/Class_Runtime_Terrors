"""Update with comments"""
# TODO Add error corection to check for invalid inputs
# TODO Refactor code to help readability
# TODO Place all code inside a main function


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
    dollar = 0.0
    stop = False
    print("Welcome to the change maker \n")
    while stop == False:
        dollar = input("Enter a dollar amount: \n")
        if float(dollar) <= 0:
            print("Please enter a valid us monetary value (i.e, 1.73) \n")
        else:
            convert(dollar)
            convert_again = input(
                "Would you like to convert more money? Type y or n: \n")
        if convert_again.lower() == 'n':
            stop = True
            print("Goodbye")


change_maker_5000()
