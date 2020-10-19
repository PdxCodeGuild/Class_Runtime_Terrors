

def convert(dollars):

    coins = [
        ('half-dollar', .50),
        ('quarter', .25),
        ('dime', .10),
        ('nickel', .05),
        ('penny', .01)]

    for coin, i in coins:
        if dollars // i:
            #print(f"yes {coin}")
            dollars = processor(coin, i, dollars)
        else:
            print(f" 0 {coin}")


def processor(coin, i, dollar):
    count = dollar // i
    dollar = dollar - (count * i)
    dollar = round(dollar, 3)
    print(f'{count}  {coin}')
    return dollar


def main():
    stop = False
    while stop == False:

        print("Welcome to coin converter version 2!")
        money = input("please enter a dollar amount:")
        money = float(money)
        convert(money)
        convert_again = input(
            "Would you like to convert more money? n for no or y for yes: \n")
        if convert_again.lower() == 'n':
            print("Goodbye.")
            stop = True


main()
