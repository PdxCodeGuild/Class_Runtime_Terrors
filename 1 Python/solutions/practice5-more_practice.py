# Practice 5: More Practice
# Problem 1: Pretty Numbers
# Convert an integer into a pretty string with commas 12345678 to 12,345,678

def pretty_number(num):
    # Get length of argument - gives back integer
    str_num = str(num)

    # find out how many commas are needed
    counter = 0
    num_list = []

    for i in range(len(str_num)-1, -1, -1):
        # adding each element from str_num to empty list
        num_list.append(str_num[i])
        counter += 1

        # checks if counter is 2, and adds comma
        if counter == 3:
            num_list.append(',')
            counter = 0

    num_list.reverse()

    return ''.join(num_list)
            
# print(pretty_number(12345678)) # 12,345,678

# non-modulus version:
def make_pretty_helper(input):
    output = input
    if len(output) < 4:
        return output
    output = [char for char in output]
    decrementer = len(output) - 3
    while decrementer >= 0:             #01234567
        output.insert(decrementer, ',') #1000000                          
        decrementer -= 3                #1000,000
    return ''.join(output)

# print(make_pretty_helper('12345678'))


# Problem 2: Pretty Bytes
# Convert a number of bytes 1567123 into a pretty form 1.5 mb. The round function can take two parameters, the number and the number of decimal places to round to print(round(1.2345, 2)) will print 1.23.
def pretty_bytes(num, digits):
    # print(round(1.2345, 2))

    # if type(round_length) != int or type(round_length) != float:
    #     print('MADE IT!')

    # < 1e3 == bytes
    if num < 1e3: 
        return f'{num} b'
    # < 1e6 == kilobytes
    elif num < 1e6:
        return f'{round((num/1000), digits)} kb'
    # < 1e9 == megabytes
    elif num < 1e9:
        return f'{round((num/1000000), digits)} mb'
    # < 1e12 == gigabytes
    elif num < 1e12:
        return f'{round((num/1e9), digits)} gb'
    # < 1e15 == terabytes
    elif num < 1e15:
        return f'{round((num/1e12), digits)} tb'


# print(pretty_bytes(999, 2)) # 200 b
# print(pretty_bytes(1000, 2)) # 1.0 kb
# print(pretty_bytes(1567123, 2)) # 1.6 mb
# print(pretty_bytes(7321000000, 2)) # 7.32 gb
# print(pretty_bytes(7321000000100, 2)) # 7.32 gb
