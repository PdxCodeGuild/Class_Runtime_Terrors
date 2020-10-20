# 10/16/2020

print("Welcom to the Change Maker 5000 (tm)")

def change_calc():
    amount = float(input("Enter a dollar amount: "))*100
    quarter = int(amount//25)
    amount -= quarter*25
    dime = int(amount//10)
    amount -= dime*10
    nickel = int(amount//5)
    amount -= nickel*5
    penny = int(amount//1)
    print(f"{quarter} quarters, {dime} dime, {nickel} nickel, {penny} penny")

change_calc()
proceed = "yes"
proceed = input("Would you like to make more change? ")
while proceed == "yes":
    change_calc()
else:    
    print("Have a good day!")

# Version 2
Coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
print(Coins[0][1])