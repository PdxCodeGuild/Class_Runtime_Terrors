# PDX Fullstack Week One Lab One Ver.1

def main():
    # get user input some number x for the number of feet to convert to meters
    x = input("How many feet? ")
    x = float(x)
    # convert x to meters (m)
    m = 0.3048
    print(x, " ft is ", round((x * m), 4), " m")

main()
