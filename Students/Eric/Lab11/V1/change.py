
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
        ut = umoney
        uquarter = ut//.25
        ut = ut - uquarter*.25
        udime = ut//.10
        ut = ut - udime*.10
        unickle = ut//.05
        ut = (ut - unickle*.05)*100
        ut = round(ut)

        if uquarter > 1:
            print (f'{int(uquarter)} Quarter(s), ', end = '')
        if udime > .1:
            print (f'{int(udime)} Dimes(s), ', end = '')
        if unickle > .05:
            print (f'{int(unickle)} Nickle(s), ', end = '')
        if ut >= 1:
            print (f'{ut} Penny(ies), ', end = '')
        if again() == False:
            break

print('Welcome to the Change Maker 5000 (tm)')
main()
print('Have a good day!')