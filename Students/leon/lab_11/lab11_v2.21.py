# PDX Fullstack lab 11 Make Change version 2.21
# program will take user input as a dollar amount and return
# number of each type of coin necessary to equal that dollar amount
# version 2 will use a tuple for the coin values plus some custom coins
# ver 2.21 assumes coinage of the British Regency circa 1817
# useful for Jane Austen fans


def coin(x):
    '''coins = [              // full coin list for future mods
        ('monkey', 480000)    # slang. 500 pounds
        ('pony', 24000)     #slang. 25 pounds
        ('guinea', 1008),   # a gold coin minted in africa, hence the name; 1 pound 1 shilling
        ('sovereign', 960), # one pound sterling in tower ounces; abrv. 'l' from latin librum; 
        ('ten bob note', 480), 
        ('crown', 240),     
        ('half crown', 120), # 1 florin and 1 sixpence
        ('florin', 24),     # 2 schillings
        ('shilling', 48),   # abrv. 's.'; 1/12 of a silver pound
        ('sixpence', 24),   # a 6 penny bit
        ('thrupenny', 12),  # a 3 penny bit
        ('penny', 4),       # abrv. 'p'.; 1/240 of a silver pound
        ('ha_penny', 2),    # 0.5 penny
        ('farthing', 1)     # 0.25 penny

        ]'''
    coins = [   
        ('sovereign', 960),     # 1 pound sterling silver
        ('shilling', 48),       # 1/12 of a pound 
        ('penny', 4),           # 1/20 of a shilling     
        ('farthing', 1)         # 1/4 of a penny
        ]
    
    v = 0
    i = 0
    for v in coins:
        for i in v:
            if (x >= v[1]):
                y = v[1]
                coin = (x // y)
                x = x - (coin * y)
                return(coin)
            # else: 
            #    return(0)
    

def main():
    endgame = False
        
    print("Welcom to Regency Change Maker.")
    print("We will exchange your 2019 USD to 1817 British Sterling.")
    while not endgame: 
        sovereign = 0
        shilling = 0
        penny = 0
        farthing = 0
        x = input("Enter the amount of dollars: ")
        x = float(x)
        x = x * 1.295 # converts from 2019 USD to 2019 GBP
        x = x * 73.76 # converts from 2019 GBP to purchasing parity value of 1817 pounds-sterling
        x = x * 240 # converts from pounds to pennies
        x = x * 4 # converts from pennies to farthings
        x = int(x)
        #print(x)

        while x > 0:
            if x > 959:
                sovereign = ((coin(x)))
                x = x - (sovereign * 960)
            if x > 47:
                shilling = ((coin(x)))
                x = x - (shilling * 48)
            if x > 3:
                penny = ((coin(x)))
                x = x - (penny * 3)
            else: 
                farthing = ((coin(x)))
                x = x - (farthing)
        
        print(f'''
        {sovereign} pounds,  
        {shilling} shillings,
        {penny} pennies, and 
        {farthing} farthings.\n
        ''')

        end = input("Need more change? y/n: ").lower()
        if end == 'n':
            endgame = True
            
            break
        
    print("Thank you.")   

main()
