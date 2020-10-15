user_input_number= input("Please enter a number to be converted: ")
user_input_units = input("Please enter the units of the number to be converted: ft, miles, meters, km, yards, inches \n >")
user_input_number = float(user_input_number)
if user_input_units == "meters":
    print(f"{user_input_number} {user_input_units} is {user_input_number} {user_input_units}")
elif user_input_units == "ft":
    foot = user_input_number * 0.3048
    print (f"{user_input_number} {user_input_units} is {foot} meters")
elif user_input_units == "miles":
    miles = user_input_number * 1609.34
    print (f"{user_input_number} {user_input_units} is {miles} meters")
elif user_input_units == "km":
    km = user_input_number * 1000
    print(f"{user_input_number} {user_input_units} is {km} meters")
elif user_input_units == "inches":
    inches = user_input_number * 0.0254
    print (f"{user_input_number} {user_input_units} is {inches} meters")
elif user_input_units == "yards":
    yards = user_input_number * 0.9144
    print(f"{user_input_number} {user_input_units} is {yards} meters")


# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m