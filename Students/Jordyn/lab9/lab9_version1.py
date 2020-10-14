conversions = {'feet':0.3048}

user_input = int(input("How long is your measurement?\n>"))
length_in_meters = user_input * conversions['feet']

length_in_meters = round(length_in_meters, 2)

print(length_in_meters, " meters.")