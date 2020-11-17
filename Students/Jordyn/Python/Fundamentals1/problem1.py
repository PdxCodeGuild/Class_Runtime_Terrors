def is_even(value):
    value = abs(value % 2)
    if value > 0:
        return 'Is odd'
    elif value == 0:
        return 'Is even'

value = int(input('Input a whole number: '))

response = is_even(value)

print(response)