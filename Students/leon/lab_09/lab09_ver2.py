# PDX Fullstack Week One Lab One Ver.2

def main():
    # conversion data
    conv = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
    }
    # get user input for some number x of units
    x = input("HWhat is the distance? ")
    x = float(x)
    # get user input for the starting unit to convert to meters
    unitx = input("What are the units? ")
    # error check
    if unitx not in conv: 
        print("I don't understand.")
        unitx = input("What are the units?")
    # get conversion factor (f) from data in library
    f = conv.get(unitx)
    # convert x to meters (m)
    m = x * f
    print(x, unitx, " is ", round((m), 4), " m")

main()