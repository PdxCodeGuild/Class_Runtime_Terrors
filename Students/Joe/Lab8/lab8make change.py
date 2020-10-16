#version 1
desired = int(input('Please enter in pennies, the amount of money desired for conversion: '))
quarters = desired // 25
desired -= quarters * 25

dimes = desired // 10
desired -= dimes * 10

nickles = desired // 5
desired -= nickles * 5

pennies = desired

print('quarters will be ' + str(quarters))
print('dimes will be ' + str(dimes))
print('nickles will be ' + str(nickles))
print('pennies will be ' + str(pennies))


#version 2
desired = input('Please tell me the amount you want to convert: ')
desired = int(float(desired)*100)  # convert it to pennies

quarters = desired // 25
desired -= quarters * 25

dimes = desired // 10
desired -= dimes * 10

nickles = desired // 5
desired -= nickles * 5

pennies = desired

print('quarters will be ' + str(quarters))
print('dimes will be ' + str(dimes))
print('nickles will be ' + str(nickles))
print('pennies will be ' + str(pennies))
