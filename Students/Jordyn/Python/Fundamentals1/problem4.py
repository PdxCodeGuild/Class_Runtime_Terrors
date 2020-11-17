def maximum_of_three(a, b, c):
    value_list = sorted([a, b, c], reverse=True)
    return value_list[0]

a = int(input('Input a number: '))
b = int(input('Input another number: '))
c = int(input('Input one last number: '))
maximum = maximum_of_three(a, b, c)
print(f'{maximum} was the highest inputted value.')