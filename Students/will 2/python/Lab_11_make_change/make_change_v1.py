print("""
Welcome to the Change Maker 5000
""")

while True: 
    dollars = input("Please, enter a dollar amount: $")
    dollars = float(dollars)
    
    coins = [("quarter", 25), ("dime", 10), ("nickel", 5), ("penny", 1)]
    [q,d,n,p]=coins
    cents = dollars * 100

    def cascade(coin,value)
        coin = cents // value
        coin = int(coin)
        slag = cents % value
        return slag  
              
    quarter = cents //  25
    quarter = int(quarter)
    slag = cents % 25
    print(slag)

    dime =  slag // 10
    dime = int(dime)
    slag = slag % 10

    nickel = slag // 5
    nickel = int(nickel)
    slag = slag % 5

    penny = slag // 1
    penny = int(penny)

    print(f"""
    {quarter} quarters, 
    {dime} dimes, 
    {nickel} nickels
    {penny} pennies
    """)
    again = input("Would you like make more change? y/n >>> ")
    
    if again == "y":
        continue
    else:
        print ("have a good day!")
        break

"""    
    def plural(): #make a function for pluralizing printed statements
        if quarter > 1:
            return "s"

    def plural_single(coin , coin[1]):    
        if coin[1] > 1:
            if coin[0] != "penny":
                return (f"{coin[0]}s")
            else:
                return "pennies"      
        elif coin < 1:
            return ""
        elif coin == 1:
            return "{coin}"
 """