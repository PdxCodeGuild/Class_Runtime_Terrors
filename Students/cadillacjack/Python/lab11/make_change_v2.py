'''
Written by James Keicher
This is a Cadillac Jack Production
Completed : 10/19/20
'''

print('''
Welcome to Cadillac Jacks Change maker.

You will be prompted to enter a Dollar amount.
For less than $1, enter the amount as a decimal;
I.E. 67 cents is equal to ".67"
For any value over $1; 
Enter the whole dollars followed by the remainder in decimal form,
I.E. 4 Dollars and 67 cents is equal to "4.67"
''')

coins = [("quarter", .25),
("dime", .1),
("nickel", .05),
("penny", .01),
]

def convert(dollars,i):
    q= dollars // i
    d = dollars - q * i
    return q, float("{:.2f}".format(d))
def main():
    initiate = input("Would you like to use the Change Maker? y/n : ")
    while True:
        if initiate == "y":

            dollars = float(input("What is the amount you would like to convert? : "))

            for i in coins:
                if i[0] == "quarter":
                    print(f"Quarters : {convert(dollars,i[1])[0]}")
                    dollars = convert(dollars,i[1])[1]
            
                elif i[0] == "dime":
                    print(f"Dimes : {convert(dollars,i[1])[0]}")
                    dollars = convert(dollars,i[1])[1]
            
                elif i[0] == "nickel":
                    print(f"Nickels : {convert(dollars,i[1])[0]}")
                    dollars = convert(dollars,i[1])[1]
            
                elif i[0] == "penny":
                    print(f"Pennies : {dollars * 100}")
            
            initiate = input("Would you like to make more change? y/n : ")

        elif initiate == "n":
            print("Thank you for using Cadillac Jacks Change Maker.\nGoodbye!")
            break
        
        else:
            print("Please enter either a 'y' for Yes, or a 'n' for No")

main()