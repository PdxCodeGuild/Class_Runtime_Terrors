



# def add(a, b):
#     return a + b
# print(add(5, 7)) # 12

# add = lambda a, b: a + b
# print(add(5, 7)) # 12






# print('hello')
# print('hello', end='!')
# print('world')
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



# def add(a, b):
#     return a + b
# print(add(5, 7))
# a = add
# print(a(5, 7))


# def perform_operation(nums):
#     output = []
#     for num in nums:
#         output.append(num*2)
#     return output
# print(perform_operation([1, 2, 3]))


# def double(x):
#     return x*2

# def perform_operation(nums, func):
#     output = []
#     for num in nums:
#         output.append(func(num))
#     return output
# print(perform_operation([1, 2, 3], double))


# def perform_operation(nums, func):
#     output = []
#     for num in nums:
#         output.append(func(num))
#     return output
# print(perform_operation([1, 2, 3], lambda x: x*2))



text = 'The person went to the store to buy a store the.'
word_dict = {'the': 3, 'person': 1, 'went': 1, 'to': 2, 'store': 2, 'a': 1}

# words = list(word_dict.items()) # .items() returns a list of tuples
# print(words)
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(3, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])


import string
import requests
import random

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
# print(response.content.decode('utf-8').split())
response.encoding = 'utf-8'
text = response.text
text = text.lower()
text = text.replace('--', ' ')
text = text.replace('”', '\"')
text = text.replace('“', '\"')
words = text.split()
words = [word.strip(string.punctuation) for word in words]
words = words[:10000]
pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
# pair_counts = {}
# for pair in pairs:
#     pair_counts[pair] = pair_counts.get(pair, 0) + 1
#     # if pair in pair_counts:
#     #     pair_counts[pair] += 1
#     # else:
#     #     pair_counts[pair] = 1
# print(pair_counts)

following_words = {}
for word in words:
    following = []
    for pair in pairs:
        if pair[0] == word and pair[1] not in following:
            following.append(pair[1])
    following_words[word] = following

word = random.choice(list(following_words.keys()))
for i in range(100):
    print(word, end=' ')
    word = random.choice(following_words[word])








