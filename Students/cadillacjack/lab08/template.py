coin = [
("Fifty cent piece", .5),
("Quarter", .25),
("Dime", .1),
("Nickel", .05),
("Penny", .001)
]
value = new_value

def tuple_access(some_list, variable_name):
    for i in some_list:
        if i[0] == variable_name:
            new_value = i[1]
            return new_value


def quarters(how_much,value):
    amount_quarters = how_much // value
    # dimes = (quarters * .25 - how_much) // coins[2]
    return amount_quarters


def main():    
    how_much = float(input('''
What is the Dollar amount you would like to convert?
For less than $1, enter the amount as a decimal. I.E. - 67 cents is equal to ".67"
For any value over $1, Enter the whole dollars followed by the remainder in decimal form,
I.E. 4 Dollars and 67 cents is equal to 4.67
Enter Dollar amount :     '''))

    print(quarters(how_much,value))

main()
