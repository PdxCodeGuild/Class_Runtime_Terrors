'''
Written by James Keicher
Completed 10/14/2020
This is a Cadillac Jack production
'''

# Lines 8 and 9 declare a golbal boolean value for use in the while statement
y = 1
n = 0

# Lines 12 - 18 are a dictionary used to get the values needed for the computation
convert = {
"ft": 0.03048,
"mi": 1609.34,
"m": 1.0,
"km": 1000.0,
"y": 0.9144,
"i": 0.0254}

# Lines 22 - 44 are functions used to convert the users unit into the desired unit

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

# Lines 47 - 55 ask the user if they would like to use the program
def main():
    initiate = input('''
Welcome to Cadillac Jacks Unit Conversion Program.
Written 10/13/2020

Would you like to convert a distance from
one unit of measurement to another?

Enter "y" for Yes or "n" for No - ''')
# Line 57 - ** are a while loop that allows the user
#  to utilize the program.
# "True" is using the variables in lines
#  8 and 9 to evaluate the Truthiness of 
#  the "while" loop at line 61.
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
# Line 90 converts the string returned by input from line 65
#  into a float by calling on the dictionary defined at line 12
            start = convert[initial_unit]

# Lines 94 - 110 check the input from line 77 and
#  determine which function to call
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

# Line 114 resets the value of the variable "initiate"
#  to verify Truthiness of "while" loop at line 61
            initiate = input('''
Would you like to make another conversion?
Enter "y" for Yes or "n" to Exit - ''')

# Line 120 checks Falsiness of "while" loop
#  at line 61
        elif initiate.lower() == "n":
            print("Thank you for using Cadillac Jacks Unit Conversion Program")
            break

# Line 126 prompts a user to enter a valid input if they 
# fail to enter a valid response
        else:
            print("Please enter 'y' for Yes or 'n' to Exit - ")

# Line 131 executes the "main" function and returns
#  a print statement given by a specific function from
#  lines 22 - 44
main()