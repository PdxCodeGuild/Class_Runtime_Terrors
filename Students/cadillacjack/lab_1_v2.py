# This is the user interface.
# Devoloping more in v3

y = 1
n = 0

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

        initiate = input('''
Would you like to make another conversion?
Enter "y" for Yes or "n" to Exit - ''')


    elif initiate.lower() == "n":
        print("Thank you for using Cadillac Jacks Unit Conversion Program")
        break
    else:
        print("Please enter 'y' for Yes or 'n' to Exit - ")