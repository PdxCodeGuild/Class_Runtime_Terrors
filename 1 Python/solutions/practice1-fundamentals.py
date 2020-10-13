

# def add(a, b):
#     print('before return')
#     return a + b
#     print('after return')
# c = add(5, 2)
# print(c)
# print(add(5, add(1, 1)))
# print(add(8, 1))



# def say_hello(name):
#     print('hello ' + name + '!')
# result = say_hello('Bob')
# print(result)

# def add(a, b):
#     c = a + b
#     return c
# d = add(5, 2)
# print(d)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# Problem 1
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

# 5 / 2 == 2.5
# 5 // 2 == 2

# 4 / 2 == 2
# 4 // 2 == 2

# 5 % 2 == 1
# 4 % 2 == 0

def is_even(x):
    if x%2 == 1:
        return False
    else:
        return True
    # return x%2 == 0
# print(is_even(5)) # False
# print(is_even(6)) # True

# x = int(input('enter a number: '))
# if is_even(x): # if x%2 == 0:
#     print('even')
# else:
#     print('odd')


# Problem 2
# Write a function that takes two integers, a and b, and returns True if one is positive and the other is negative, and return False otherwise.


def opposite(a, b):
    return a*b < 0

    # if a*b < 0:
    #     return True
    # else:
    #     return False

    # if a > 0 and b < 0:
    #     return True
    # elif a < 0 and b > 0:
    #     return True
    # else:
    #     return False
    
    # return (a > 0 and b < 0) or (a < 0 and b > 0)

# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False


# if a function doesn't return anything, it implicitly returns None
# fruits = ['apples', 'bananas']
# fruits.append('pears') # correct
# fruits = fruits.append('pears') # INCORRECT
# print(fruits)

# fruits = 'apples, bananas'
# fruits = fruits + ', pears'
# print(fruits)



# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100(num):
    # if abs(num - 100) <= 10:
    #     return True
    # else:
    #     return False

    # return abs(num - 100) <= 10
    # return num >= 90 and num <= 110
    return 90 <= num <= 110

# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4
# Write a function that returns the maximum of 3 parameters.


# import math
# math.floor(5.2) # 5
# math.ceil(5.2) # 6

def maximum_of_three(a, b, c):
    return max(max(a, b), c)
    # if a > b and a > c:
    #     return a
    # elif b > a and b > c:
    #     return b
    # else:
    #     return c
    
    # if a > b:
    #     if a > c:
    #         return a
    #     else:
    #         return c
    # else:
    #     if b > c:
    #         return b
    #     else:
    #         return c

# print(maximum_of_three(45, 0, 1)) # 45
# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10

# def max_list(nums):
#     if len(nums) == 0:
#         return None
#     running_max = nums[0]
#     for x in nums:
#         if x > running_max:
#             running_max = x
#     return running_max
# print(max_list([])) # None
# print(max_list([1, 2, 3])) # 3
# print(max_list([1, 4, 2, 3])) # 4
# print(max_list([1])) # 1



# Problem 5
# Write a loop to print the powers of 2 from 2^0 to 2^20

def print_powers_2():
    i = 0
    while i <= 20:
        print(2 ** i)
        i += 1
print_powers_2() # 1, 2, 4, 8, 16, 32, ...







# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 3123
# 3*10^3 + 1*10^2 + 2*10^1 + 3*10^0

# 101
# 1*4 + 0*2 + 1*1 = 5
# 1101
# 1*8 + 1*4 + 0*2 + 1*1 = 13

# 00000000
# 11111111 = 255 = 2^8-1
# 999 = 10^3-1




