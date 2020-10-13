



# fruits = ['apples', 'pears', 'bananas', 'pears']
# while 'pears' in fruits:
#     fruits.remove('pears')
# print(fruits) # ['apples', 'bananas', 'pears']


# nums = [1, 2, 3, 'a', 202, 'b']
# nums.sort()
# print(nums)


# iterators - can be used with a for loop
# strings, lists, tuples, dicts, ranges

# fruits = ['bananas', 'apples', 'pears']
# print(sorted(fruits))
# print(list(reversed(fruits)))

# for fruit in reversed(fruits):
#     ...



import random
import math
import string

# nums = []
# for i in range(100):
#     nums.append(random.randint(1,100))
# print(nums)

# nums = [random.randint(1,100) for i in range(100)]
# # print(nums)
# nums = [math.sqrt(num) for num in nums]
# print(nums)

# text = 'The person went to the store, and bought a drink.'
# text = text.split()
# text = [word.capitalize() for word in text]
# print(text)

# text = [char for char in text if char not in string.punctuation]
# print(text)
# text = '-'.join(text)
# print(text)


# even_numbers = [n for n in range(100) if n%2 == 0]
# print(even_numbers)

alphabet = 'abcdefg'
output = ''
# iterate over characters of input string
char = 'd'
print((alphabet.index(char) + 13) % len(alphabet))









