'''
Created by: James Keicher
A Cadillac Jack production
Tue, October 13 2020
'''


# Lines 10 - 14 are a dictionary used to convert the user input
# from a string to a float
convert = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1.0,
"km": 1000.0,
"yard": 0.9144,
"inch": 0.0254}

# Lines 19 - 21 are a function that multiples the user inputs

def conversion(user_distance, user_unit):
    result = float(user_distance) * user_unit
    print(f"The units you entered are equal to {result} meters.")
    
# Lines 27 - 43 are the main function that ask the user
# for values to convert. i.e.; how many meters is 5 miles?
# The "main" function then converts the inputs into floats
# and sends them to the "conversion" function

def main():
    user_distance = input("Please select a distance you wish to convert: ")
    user_unit = input(
'''What is the unit you would like to convert from?
For Feet : Enter "ft"
For Miles : Enter "mi"
For Meters : Enter "m"
For Kilometers : Enter "km" :  ''')
    
    # Line 37 calls on a globally defined dictionary which 
    # has values stored for a key, the key is provided via 
    # user input in lines 29 - 36
    unit = convert[user_unit]

    # Line 41 pushes the users input into the "conversion"
    # function at line 18
    conversion(user_distance, unit)
# Line 43 executes the program
main()    