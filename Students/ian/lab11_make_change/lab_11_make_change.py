"""
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.
"""
def floorAndSubtract(curr, val):
    ret = curr // val
    rem = curr - ret * val
    if rem < 0:
        return curr, 0
    return rem , int(ret)
    
def makeChange(val):
    if not val or val < 0:
        return
    val, quarters = floorAndSubtract(val, .25)
    val, dimes = floorAndSubtract(val, .1)
    val, nickles = floorAndSubtract(val, .05)
    val, pennies = floorAndSubtract(val, .01)
    return f"{quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies"
def makeChangev2(total):
    coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
    ]
    ret = []
    for name, val in coins:
        total, t = floorAndSubtract(total, val/100)
        if t > 0:
            ret.append(str(t) + " " + name + " ")
    return ", ".join(ret)
    




def main():
    print("Welcome to Change Maker\n")
    while True:
        n = float(input("Enter a dollar amount: "))
        print(makeChangev2(n))
        r = input("Would you lke to make more change? (no)")
        if r.lower() == "no":
            break

main()