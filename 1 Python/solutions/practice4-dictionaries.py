## Problem 1

# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

# def has_key(d, key):
#     #alt version: return key in d - both methods return Boolean
#     # if key in d:
#     #     return True
#     # else:
#     #     return False

#     for k in d:
#         if key == k:
#             return True
#     return False
    
# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False

## Problem 2
# Write a function that returns True if the given dictionary is empty, False otherwise.
# python


def is_empty(d):
    # return len(d) == 0
    if len(d) > 0:
        return False
    else:
        return True


# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False


## Problem 3
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return None.
def find_key(d, value):


    for key in d:
        if d[key] == value:
            return key
    # return None - this line isn't NECESSARY, but makes the code more readable and explicit

    # value_list = list(d.values())
    # print(value_list)


# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None

## Problem 4
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed
def reverse_dict(d):
    reversed_dict = {}
    for key in d:
        reversed_dict[d[key]] = key
    return reversed_dict

# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}

## Problem 5
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.
def merge(list1, list2):
    empty_dict = {}
    for i in range(len(list1)):
        empty_dict[list1[i]] = list2[i]
    return empty_dict
# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}