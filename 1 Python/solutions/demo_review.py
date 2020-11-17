


# while loops ===========================================

# while loop - loop 10 times
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# while loop - iterate over the indices of a string
#       01234
# word = 'hello'
# i = 0
# while i < len(word):
#     print(word[i])
#     i += 1

# while loop - iterate over the indices of a list
# fruits = ['apples', 'bananas', 'pears']
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1


# indefinite loop w/ break
# num = None
# while True:
#     num = input('enter a number: ')
#     if num.isdigit():
#         num = int(num)
#         break
#     else:
#         print('that\'s not a number')
# print(num)


# indefinite loop w/ a boolean flag
# not_valid = True
# num = None
# while not_valid:
#     num = input('enter a number: ')
#     if num.isdigit():
#         num = int(num)
#         not_valid = False
#     else:
#         print('that\'s not a number')
# print(num)


# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# iterables - range, string, list, tuple, dictionary

# x = list(range(100))

# x = []
# for i in range(100):
#     x.append(i)



# x = list(reversed('abc'))
# print(x)



# for loops =====================================

# range w/ 1 number - upper bound
# it will go from 0 up to but not including 10
# for i in range(10):
#     print(i)

# range w/ 2 numbers - lower bound, upper bound
# it will go from 5 up to but not including 10
# for i in range(5, 10):
#     print(i)

# range w/ 3 numbers - lower bound, upper bound, increment
# it will go from 5 up to but not including 10
# for i in range(10, 20, 2):
#     print(i)
# for i in range(20, 9, -2):
#     print(i)

# iterating over the indices of the characters in a string
#       0123456789...
# text = 'hello world!'
# print(len(text))
# for i in range(len(text)):
#     print(i, text[i])

# iterating over the indices of the elements in a list
#            0          1         2
# fruits = ['apples', 'bananas', 'pears']
# for i in range(len(fruits)):
#     # print(i, fruits[i])
#     fruits[i] += '!'
# print(fruits)

# iterating over the elements of a list directly
# fruits = ['apples', 'bananas', 'pears']
# print(fruits)
# for fruit in fruits:
#     print(fruit)
    # index = fruits.index(fruit)
    # fruits[index] += '!'
# print(fruits)

# text = 'hello world!'
# for char in text:
#     print(char)



# accumulator pattern
# import random
# import string
# pw_length = int(input('what is the length of your password? '))
# password = ''
# for i in range(pw_length):
#     password += random.choice(string.ascii_letters + string.digits + string.punctuation)
# print(password)



# x = 5 # declaration and assignment
# x = 10 # just an assignment


# this will always crash
# if (temperature > 80) {
#     let output = 'hot'
# } else if (temperature > 60) {
#     let output = 'warm'
# }
# console.log(output)

# scope is the region of code in which a variable is visible
# temperature = 50
# output = None
# if temperature > 80:
#     output = 'hot'
# elif temperature > 60:
#     output = 'warm'
# else:
#     output = 'cold'
# print(output)

# x = 'hello'
# for i in range(10):
#     x += '!'
# print(x)


# def add(a, b):
#     # print(a)
#     # print(b)
#     c = a + b
#     return c
# print(add(5, 7))
# print(c)

# print(x)
# x = 10

