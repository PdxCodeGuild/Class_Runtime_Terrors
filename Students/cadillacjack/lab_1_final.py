# This is the user interface.
# Devoloping more in v3

y = 1
n = 0

convert = {
"ft": 0.03048,
"mi": 1609.34,
"m": 1.0,
"km": 1000.0,
"y": 0.9144,
"i": 0.0254}



def to_feet(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["ft"]
    print(f"The units you entered are equal to {result} Feet.")

def to_miles(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["mi"]
    print(f"The units you entered are equal to {result} Miles.")

def to_kilometers(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["km"]
    print(f"The units you entered are equal to {result} Kilometers.")

def to_yards(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["y"]
    print(f"The units you entered are equal to {result} yards.")

def to_inches(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["i"]
    print(f"The units you entered are equal to {result} inches.")

def to_meters(user_distance, user_unit):
    result = float(user_distance) * user_unit
    print(f"The units you entered are equal to {result} meters.")

def main():
    initiate = input('''
Welcome to Cadillac Jacks Unit Conversion Program.
Written 10/13/2020

Would you like to convert a distance from
one unit of measurement to another?

Enter "y" for Yes or "n" for No - ''')
    while True:
        if initiate.lower() == "y":
            number = input("Enter the distance to be converted : ")

            initial_unit = input('''
What is the starting unit of measurement?

Enter "i" for Inches
Enter "ft" for Feet
Enter "y" for Yards
Enter "mi" for Miles
Enter "m" for Meters
Enter "km" for Kilometers

Starting Unit - ''')
        
            desired_unit = input('''
How would you like the measurement to be displayed?

Enter "i" for Inches
Enter "ft" for Feet
Enter "y" for Yards
Enter "mi" for Miles
Enter "m" for Meters
Enter "km" for Kilometers

Final Unit - ''')

            start = convert[initial_unit]
            
        

            if desired_unit == "m":
                to_meters(number, start)

            elif desired_unit == "i":
                to_inches(number, start)

            elif desired_unit == "ft":
                to_feet(number, start)

            elif desired_unit == "y":
                to_yards(number, start)

            elif desired_unit == "mi":
               to_miles(number, start)

            elif desired_unit == "km":
                to_kilometers(number, start)


            initiate = input('''
Would you like to make another conversion?
Enter "y" for Yes or "n" to Exit - ''')

        elif initiate.lower() == "n":
            print("Thank you for using Cadillac Jacks Unit Conversion Program")
            break

        else:
            print("Please enter 'y' for Yes or 'n' to Exit - ")

main()