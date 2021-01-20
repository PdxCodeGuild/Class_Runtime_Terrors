# PDX Fullstack Week One Lab One Ver.2

def main():
    # conversion data
    conv = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }
    # get user input for some number x of units
    x = input("HWhat is the distance? ")
    x = float(x)
    # get user input for the starting unit to convert to meters
    unitx = input("What units to start? ")
    # error check
    if unitx not in conv: 
        print("I don't understand.")
        unitx = input("What are the units?")
    unity = input("What units to find? ")
    # error check
    if unity not in conv: 
        print("I don't understand.")
        unity = input("What units to find?")
    # get conversion factor-1 (f1) from data in library
    f1 = conv.get(unitx)
    # convert x to meters (m)
    m = x * f1
    # get conversion factor-2 (f2) from data in library
    f2 = conv.get(unity)
    # convert meters(m) to final unit (final)
    final = m / f2
    print(x, unitx, " is ", round((final), 4), unity)

main()