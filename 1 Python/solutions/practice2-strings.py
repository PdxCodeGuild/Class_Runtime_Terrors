
# Problem 1 =========================================
# Return the number of letter occurances in a string.

def count_letter(letter, word):
    letter_count = 0
    for char in word:
        if char == letter:
            letter_count += 1
    return letter_count

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2



# Problem 2 =======================================

# print(ord('a')) # 97
# print(ord('b')) # 98
# print(chr(97)) # 'a'

# #      01234
# print('hello'.index('o')) # 4


# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    base = 97 
    for char in word:
        base = max(base, ord(char))
        #print(char, ord(char))
    base = chr(base)
    return base

    # word = list(word)
    # word.sort()
    # # return word[-1]
    # return word[len(word)-1]

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # running_max = 0
    # for char in word:
    #     index = alphabet.index(char)
    #     # print(char, index)
    #     # running_max = max(running_max, index)
    #     if index > running_max:
    #         running_max = index
    # return alphabet[running_max]

# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v




# Problem 3 ======================================================

# Write a function that returns the number of occurances of 'hi' in a given string.


# print('hello world world world'.find('world')) # 6
# print('hello world world world'.find('world', 7)) # 12
# print('hello world world world'.find('world', 13)) # 18
# print('hello world world world'.find('world', 19)) # 18

import re

def count_hi(text):
    # return text.count('hi')

    # count = 0
    # starting_index = 0
    # while True:
    #     index = text.find('hi', starting_index)
    #     if index == -1:
    #         break
    #     count += 1
    #     starting_index = index + 1
    # return count

    # results = re.findall('hi', text)
    # return len(results)

    count = 0
    for i in range(len(text)-1):
        # print(len(text), i, i+1)
        # text[i+1]
        if text[i] == 'h' and text[i+1] == 'i':
            count += 1
    return count

#               0123
print(count_hi('hihih')) # 2
print(count_hi('hello23hi45world hi 123abcllamama hi')) # 3



# falsey values: 0, '', [], {}, None, False
# everything else is truthy


# values = [0, 1, '', 'hi', [], ['hi'], {}, {'a':1}]
# for value in values:
#     print(value, 'is', end=' ')
#     if value:
#         print('truthy')
#     else:
#         print('falsey')



# Problem 5
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).
​
​
# this_is_snake_case (python)
# thisIsCamelCase (java, javascript, c#)
# ThisIsPascalCase (python classes)
# this-is-kebab-case (css)
​
​
#text.replace(char.ascii)
#string.ascii_punctuation()
​
import string
​
​
def snake_case(text):
    output_string = ''
    for char in text:
        if char not in string.punctuation:
            output_string += char
    output_string = output_string.lower()
    output_string = output_string.replace(' ', '_')
    #text = text.replace(string.punctuation, '')
    return output_string
#print(snake_case('@Hello % World!@#$!')) # hello_world
#print(string.punctuation)
​
​
# Problem 6
​
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).
​
​
​
​
def camel_case(text):
    output_string = ''
    text = text.lower() 
    #remove punctuation
    for char in text:
        if char == ' ' or char not in string.punctuation:
            output_string+= char
    output_string_the_second = ''
    list_output = output_string.split(' ')
    for i in range(len(list_output)):
        list_output[i] = list_output[i].capitalize()    
    list_output[0] = list_output[0].lower()
    output_string_the_second = ''.join(list_output)
    #
    # for i in range(len(output_string) - 1): #last letter?
    #     if output_string[i] == ' ':
    #         output_string_the_second += output_string[i+1].upper()
    #         i += 1
    #     else:
    #         output_string_the_second += output_string[i]
    return output_string_the_second   
print(camel_case('Hello World!')) # helloWorld
print(camel_case('This is another example.')) # thisIsAnotherExample
​
​
​
# mylist = ['apples', 'bananas', 'pears']
# mylist[0] = 'cherries'
# for i in range(len(mylist)):
#     mylist[i] = mylist[i].capitalize()
#     #mylist[i] = mylist[i] + '!'
# print(mylist)
​
​
# x = mylist[0]
# x = 'hello!'
# print(mylist[0])
​
# for element in mylist:
#     element = 'hello!'
# print(mylist)
​
# tester_string = "I love pizza!"
# list_strings = tester_string.split(" ")
# print(list_strings)
# joined_strings = ''.join(list_strings)
# print(joined_strings)
​
#"abcdefg"
​
#       01234
# text = 'hello'
# for char in text:
#     print(char)
# for i in range(len(text)):
#     print(i, text[i])
# 0123
#'hihi'
# def count_hi(text):
#     count = 0
#     for i in range(len(text)-1):
#         # print(len(text), i, i+1)
#         # text[i+1]
#         if text[i] == 'h' and text[i+1] == 'i':
#             count += 1
#     return count

def alternating_case(text):
    output = ''
    alternating = False
    for char in text:
        # if alternating:
        #     output += char.upper()
        # else:
        #     output += char.lower()
        output += char.upper() if alternating else char.lower()
        alternating = not alternating
    return output
print(alternating_case('Hello World!')) # HeLlO WoRlD!
print(alternating_case('This is another example.')) # ThIs iS AnOtHeR ExAmPle.
