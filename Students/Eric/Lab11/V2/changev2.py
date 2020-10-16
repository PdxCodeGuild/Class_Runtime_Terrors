coins = {
    'half-dollar': 50,
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}


def userinput():
    while True:
     x = input('Enter a dollar amount:')
     try:
          x = float(x)    
          return (x)
     except:
          print('\nInvaid input try again!')

def again():
    while True:
        again = input('\nWould you like make more change(Y or N): ').lower()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print('Only \'y\' or \'n\' inputs are vaild')

def main():
    while True:
        umoney = userinput()
        ut = umoney*100
        for x in coins:
            moneynow = (ut//coins[x])
            if moneynow > 0:
                print (f'{moneynow} {x} ', end = '')
            ut = ut - (moneynow * coins[x])

        if again() == False:
            break

print('Welcome to the Change Maker 5000 (tm)')
main()
print('Have a good day!')