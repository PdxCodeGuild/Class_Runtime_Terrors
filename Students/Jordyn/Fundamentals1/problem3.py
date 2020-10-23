def near_100(value):
    upper = 111
    lower = 90
    if value in range(lower, upper):
        return True
    elif value not in range(lower, upper):
        return False

value = int(input('Please input a number: '))
print('Is value within 10 numbers of 100?')
value = near_100(value)
print(value)