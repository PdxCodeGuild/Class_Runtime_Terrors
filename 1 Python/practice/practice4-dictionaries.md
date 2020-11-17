
# Practice Problems: Dictionaries


## Problem 1

Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

```python
def has_key(d, key):
    ...
print(has_key({'a': 1, 'b': 2}, 'a')) # True
print(has_key({'a': 1, 'b': 2}, 'c')) # False
```

## Problem 2

Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

```python
def is_empty(d):
    ...
print(is_empty({})) # True
print(is_empty({'a': 1, 'b': 2})) # False
```

## Problem 3

Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

```python
def find_key(d, value):
    ...
print(find_key({'a': 1, 'b': 2}, 1)) # a
print(find_key({'a': 1, 'b': 2}, 3)) # None
```

## Problem 4

Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

```python
def reverse_dict(d):
    ...
print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}
```

## Problem 5

Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

```python
def merge(list1, list2):
    ...
print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}
```


## Problem 6

Write a function that merges two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

```python
def merge(list1, list2):
    ...
print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}
```

## Problem 7

Write a function that takes a dictionary and returns a new dictionary without values less than 10.

```python
def remove_less_than_10(d):
    ...
print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}
```

## Problem 8

Write a function to calculate the average of the lists in a dictionary.

```python
def average_values(d):
    ...
print(average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]})) # {'a': 4, 'b': 5, 'c': 3}
```

## Problem 9

Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key

```python
def merge_dictionaries(d1, d2):
    ...
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(merge_dictionaries(d1, d2)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
```

## Problem 10

Write a function that takes a list of strings and counts of the number of occurances.

```python
def count_votes(votes):
    ...
votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
print(count_votes(votes)) # {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}
```




