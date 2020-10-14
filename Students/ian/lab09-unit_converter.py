def main():
    distance  = input("What is the distance? ")
    in_units = input("What are the input units? ")
    out_units = input("What are the output units? ")
    dis = ""
    unit_con = 1
    try:
        dis = float(distance)
        if(in_units == out_units):
            unit_con = 1
        elif in_units == "ft":
            if out_units == "m":
                unit_con= 0.3048
        elif in_units == "mi":
            if out_units == "m":
                unit_con= 1609.34
        elif in_units == "m":
            if out_units == "ft":
                    unit_con= 1/0.3048
            if out_units == "mi":
                    unit_con= 1/1609.34
            if out_units == "km":
                    unit_con= 1/1000
        elif in_units == "km":
            if out_units == "m":
                    unit_con= 1000
        else:
            raise Exception("no matching type")
    except:
        print("Bad type")
        exit(1)
    print(distance, in_units, " is ", dis * unit_con, out_units)

if __name__ == '__main__':
    main()