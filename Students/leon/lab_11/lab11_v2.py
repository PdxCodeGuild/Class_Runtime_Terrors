# PDX Fullstack lab 11 Make Change version 2
# program will take user input as a dollar amount and return
# number of each type of coin necessary to equal that dollar amount
# version 2 will use a tuple for the coin values plus some custom coins



def coin(x):
    coins = [
        ('quarter', 25),
        ('dime', 10),
        ('nickel', 5),
        ('penny', 1)
        ]
    
    for v in coins:
        for i in v:
            if x > v[1]:
                y = v[1]
                return (x // y)
    

def main():
    print("Welcom to Change Maker")
    x = input("Enter the dollar amount: ")
    x = float(x)
    x = x * 100
    x = int(x)
    print(x)

    while x > 0:
        if x > 25:
            print((coin(x)), " quarters, ")
            x = x - (coin(x) * 25)
        if x > 10:
            print((coin(x)), " dimes, ")
            x = x - (coin(x) * 10)
        if x > 25:
            print((coin(x)), " nickles, ")
            x = x - (coin(x) * 5)
        if x > 1: 
            print((coin(x)), " pennies.\n")
            x = x - (coin(x) * 1)
   

main()
