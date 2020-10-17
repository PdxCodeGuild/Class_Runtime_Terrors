#Cleon
#Lab 11: Make Change
# Version 2

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]


def anotherOne():
    while True:
        again = input("Would you like to make more change? ")
        if again == "yes" or again == "y":
            return True
        elif again == "no" or again == "n":
            return False
        else:
            continue            


def main():
    while True:
        user_money = float(input("Enter a dollar amount: "))
        new_money = user_money * 100 # removes decimal place, so you can use floor function more effectively..Stores user input in new_money 
        for x in coins: # loops thorugh list - remember it's a LIST of TUPLES with two elements in each tuple
            remainder = new_money // x[1] # x[1] is the second element in the current tuple!  - money is floor divided by a coin - remember it's interating thorugh list - that is what i mean by current 
            if remainder == 0: # if current coin can not divide  into money the skip
                continue # skip
            else:
                new_money = new_money - (remainder * x[1]) # subtracting whats been taking out
                print(f"{int(remainder)} {x[0]} ") # print coin name and how many times it divides into money

        if anotherOne() == False:       
            break
        

main()


    
            


            


    
       
        
                


    
 
           
       
    



