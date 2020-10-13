

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     # i = i + 1
# print('done')

#             0         1         2         3
# fruits = ['apples', 'bananas', 'pears', 'cherries']
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1




# people = ['bob', 'jim', 'mary', 'jane']
# person = input('who are you looking for? ')
# i = 0
# while i < len(people):
#     # print(person, people[i])
#     if person == people[i]:
#         print('person found')
#         break
#         # print('after the break')
#     i += 1
# else: # the else is executed if you never *break*
#     print('person not found')



# people = ['bob', 'jim', 'mary', 'jane']
# person = input('who are you looking for? ')
# person_found = False
# i = 0
# while i < len(people):
#     if person == people[i]:
#         print('person found')
#         person_found = True
#         break
#     i += 1
# if not person_found:
#     print('person not found')


import random

# REPL = read evaluate print loop
# keep_looping = True
# while keep_looping:
#     n = int(input('how many emoticons do you want? '))
#     i = 0
#     while i < n:
#         emoticon = random.choice([':', ';']) + random.choice(['-', '']) + random.choice([')', ']'])
#         print(emoticon)
#         i += 1
#     keep_looping = input('would you like to continue? ') == 'y'



# while True:
#     n = int(input('how many emoticons do you want? '))
#     i = 0
#     while i < n:
#         emoticon = random.choice([':', ';']) + random.choice(['-', '']) + random.choice([')', ']'])
#         print(emoticon)
#         i += 1
#     if input('would you like to continue? ') != 'y':
#         break



# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)

#             0        1           2
# iterating over the indices of a list
fruits = ['apples', 'bananas', 'pears']
for i in range(len(fruits)):
    print(fruits[i])


# iterating over the elements
for fruit in fruits:
    print(fruit)

text = 'hello!'
for char in text:
    if char == 'l':
        print('!')
        continue
    print(char)


# lower = 5
# upper = 10
# increment = 1
# i = lower
# while i < upper:
#     print(i)
#     i += increment
# for i in range(lower, upper, increment):
#     print(i)



