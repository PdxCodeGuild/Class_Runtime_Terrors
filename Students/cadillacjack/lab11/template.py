quarter = .250
dime = .10
nickel = .050
penny = .010

def quarters(dollars,):
    q= dollars // quarter
    d = dollars - q * quarter
    return q, float("{:.2f}".format(d))

def dimes(dollars,): 
    di = dollars // dime
    do = dollars - di * dime
    return di, float("{:.2f}".format(do))

def nickels(dollars,): 
    n = dollars // nickel
    d = dollars - n * nickel

    return n,float("{:.2f}".format(d))

def pennies(dollars,): 
    p = dollars // penny
    return p


def main():
    dollars = float(input('''
Enter the amount of money you would like to convert :
For less than $1, enter the amount as a decimal;
I.E. 67 cents is equal to ".67"
For any value over $1; 
Enter the whole dollars followed by the remainder in decimal form,
I.E. 4 Dollars and 67 cents is equal to "4.67"
Enter Dollar amount : $'''))
    
    print(f"Number of Quarters : {quarters(dollars,)[0]}")
    dollars = quarters(dollars,)[1]

    print(f"Number of Dimes : {dimes(dollars,)[0]}")
    dollars = dimes(dollars,)[1]

    print(f"Number of Nickels : {nickels(dollars,)[0]}")
    dollars = nickels(dollars,)[1]

    print(f"Number of Pennies : {pennies(dollars,)}")

main()