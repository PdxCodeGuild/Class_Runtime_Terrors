
# TODO fix output at the end of money conversion
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
    # list of tuples keeps the name and value data
    coins = [
        ('half-dollar', .50),
        ('quarter', .25),
        ('dime', .10),
        ('nickel', .05),
        ('penny', .01)]
# for loop checks each coins value divisability against dollars current value
    for coin, i in coins:
        if dollars // i:
            dollars = processor(coin, i, dollars)
        else:
            print(f" 0 {coin}")

# processor takes in coin, i and dollar as arguments and for each i value passed, calculates coins, prints result and updates dollar value


def processor(coin, i, dollar):
    count = dollar // i
    dollar = dollar - (count * i)
    dollar = round(dollar, 3)
    print(f'{count}  {coin}')
    return dollar

# Main REPL


def main():
    stop = False
    while stop == False:

        print("Welcome to coin converter version 2!\n")
        money = money_handler()
        convert(money)
        stop = continue_conversion(stop)


main()
