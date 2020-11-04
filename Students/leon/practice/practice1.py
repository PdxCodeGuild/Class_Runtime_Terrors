# PDX Fullstack Practice: One
# Problem 1
# write a function that tells whether some number a is even or odd
# returns a bool
def is_even(a):
    if (a % 2):
        return False
    else:
        return True

#print(is_even(5))
#print(is_even(6))

# Problem 2: compare 2 integers - return T if one is POS and one is NEG
# else return F
def opposite(a, b):
    if (a > 0) and (b > 0):
        return False
    elif (a < 0) and (b < 0):
        return False
    else:
        return True

#print(opposite(10, -1))
#print(opposite(2, 3))
#print(opposite(-1, -1))

# Problem 3: True if num is within 10 of 100
def near_100(num):
    if ((num > 100) and ((num - 100) <= 5)) or (100 - num) <= 5:
        return True
    else:
        return False

#print(near_100(50))
#print(near_100(99))
#print(near_100(105))

# Problem 4
# return maximum of 3 variables
def maximum_of_three(a, b, c):
    return(max(a, b, c))

#print(maximum_of_three(5,6,2))
#print(maximum_of_three(-4,3,10))

# Problem 5
# print powers of 2 from 2^0 thru 2^20 using a loop
def print_powers_2():
    i = 0
    while i < 21:
        print(2 ** i)
        i += 1
    return



print_powers_2()

