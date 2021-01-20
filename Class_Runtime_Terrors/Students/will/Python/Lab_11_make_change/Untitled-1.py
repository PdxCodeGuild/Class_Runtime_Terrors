coins = [("quarter", 25), ("dime", 10), ("nickel", 5), ("penny", 1)]
[q,d,n,p]=coins

dollars = input("Please, enter a dollar amount: $ ")
dollars = float(dollars)

slag = dollars * 100

def cascade(coin,value,slag):
        change = slag // value
        slag %= value
        change = int(change)
        if coin !=  p[0]: 
            if slag > 1:
                print(f"{change} {coin}s")
            else:
                print(f"{change} {coin}") 
        elif coin == p[0]:
            if slag > 1:
                print(f"{change} pennies")
            else:
                print(f"{change} {coin}")   
        print (slag)              
        return slag
counter = 0
for x in coins:
    counter += 1 
    listslag = []
    #cascade(x[0],x[1],slag)
    print (counter, x[0])




print(cascade(q[0],q[1],slag))
print(cascade(d[0],d[1],slag))
print(cascade(n[0],n[1],slag))
print(cascade(p[0],p[1],slag))

