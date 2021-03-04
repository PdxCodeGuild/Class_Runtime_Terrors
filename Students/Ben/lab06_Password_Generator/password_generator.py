# 10/14/2020
# input, print, looping, random.choice, the 'string builder pattern'
# Version 1
import random
import string

number_lower_case = input("How many lower case letters you want in the pw: ")
number_upper_case = input("How many upper case letters you want in the pw: ")
number_special_char = input("How many special charates you want in the pw: ")

password = []

a = 1
b = 1
c = 1

while a <= int(number_lower_case):
    password.append(random.choice(string.ascii_lowercase))
    a += 1
else:
    while b <= int(number_upper_case):
        password.append(random.choice(string.ascii_uppercase))
        b += 1
    else:
        while c <= int(number_special_char):
            password.append(random.choice(string.punctuation))
            c += 1
        else:
            exit

password = ''.join(password)
print(password)

# add = lambda a, b : a + b
# print(add(5,7))

# print('hello')
# print('hello', end = ' ')

# for i in range(10):
#     print(i, end='-')

# nums = [5, 7, 2, 3]
# nums.sort()
# print(nums) # [2, 3, 5, 7]
# nums.sort(reverse=True)
# print(nums) # [7, 5, 3, 2]

# words = ['zebra', 'apple', 'chartreuse', 'strudle', 'dayz']
# words.sort()
# print(words) # ['apple', 'chartreuse', 'dayz', 'strudle', 'zebra']
# words.sort(key=lambda word: word[-1])
# print(words) # ['zebra', 'apple', 'chartreuse', 'strudle', 'dayz']
# words.sort(key=lambda word: len(word))
# print(words) # ['dayz', 'zebra', 'apple', 'strudle', 'chartreuse']
# words.sort(key=lambda word: -len(word))
# print(words) # ['chartreuse', 'strudle', 'zebra', 'apple', 'dayz']
# for word in words:
#     print(-len(word))

# def perform_operation(nums):
#     output = []
#     for num in nums:
#         output.append(num*2)
#     return output
# print(perform_operation([1, 2, 3]))