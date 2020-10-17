# PDX Fullstack lab 11 Make Change version 1
# program will take user input as a dollar amount and return
# number of each type of coin necessary to equal that dollar amount

x = 0.00
q = 0
d = 0
n = 0
p = 0

def quarter(x):
    return (x // 25)
    
def dime(x):
    return (x // 10)

def nickel(x):
    return (x // 5)

def penny(x):
    return (x // 1)


def main():
    print("Welcom to Change Maker")
    x = input("Enter the dollar amount: ")
    x = float(x)
    x = x * 100
    x = int(x)
    print(x)
    q = quarter(x)
    x = x - (q * 25)
    d = dime(x)
    x = x - (d *10)
    n = nickel(x)
    x = x - (n * 5)
    p = penny(x)
    print(q, "quarters, ", d, "dimes, ", n, "nickels, ", p, "pennies.")

main()
