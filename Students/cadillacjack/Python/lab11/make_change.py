quarter = .250
dime = .10
nickel = .050
penny = .010

def quarters(dollars,):
    q= dollars // quarter
    return q

def dimes(dollars,): 
    d = dollars // dime
    return d

def nickels(dollars,): 
    n = dollars // nickel
    return n

def pennies(dollars,): 
    p = dollars // penny
    return p


def main():
    dollars = float(input('''
    How many monies do you need to convert? : '''))
    
    print("Number of Quarters :")
    print(quarters(dollars,))
    quartered = quarters(dollars,)
    dollars = dollars - (quartered * quarter)
    dollars = float("{:.2f}".format(dollars))

    print("Number of Dimes :")
    print(dimes(dollars,))
    dimed = dimes(dollars,)
    dollars = dollars - (dimed * dime)
    dollars = float("{:.2f}".format(dollars))
    
    print("Number of Nickels :")
    print(nickels(dollars,))
    nicked = nickels(dollars,)
    dollars = dollars - (nicked * nickel)
    dollars = float("{:.2f}".format(dollars))

    print("Number of Pennies : ")
    print(pennies(dollars,))

main()

