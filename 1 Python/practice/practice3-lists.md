
# Practice Problems: Lists



For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```



## Problem 1

Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

```python
def random_element(a):
    ...
print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'
```

## Problem 2

Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

```python
print(eveneven([5, 6, 2])) # True
print(eveneven([5, 5, 2])) # False
```


## Problem 3

Write a function that returns the reverse of a list.

```python
def reverse(nums):
  ...
print(reverse([1, 2, 3])) # 3, 2, 1
```

## Problem 4

Write a function to move all the elements of a list with value less than 10 to a new list and return it.

```python
def extract_less_than_ten(nums):
  ...
print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]
```

## Problem 5
Write a function to find all common elements between two lists.

```python
def common_elements(nums1, nums2):
  ...
print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]
```


## Problem 6
Write a function to combine two lists of equal length into one, alternating elements.

```python
def combine(nums1, nums2):
    ...
print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]
```


## Problem 7

Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.

```python
def find_pair(nums, target):
  ...
print(find_pair([5, 6, 2, 3], 7)) # [5, 2]
```



## Problem 8

Write a function to find the average of a list of numbers

```python
def average(nums):
    ...
print(average([1, 2, 3, 4, 5])) # 3
```

## Problem 9

Write a function to remove all empty strings from a list.

```python
def remove_empty(mylist)
    ...
print(remove_empty(['a', 'b', '', 'c', '', 'd'])) # ['a', 'b', 'c', 'd']
```


## Problem 10

Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

```python
def merge(nums1, nums2):
  ...
print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]
```


## Problem 11

Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

```python
def combine_all(nums):
  ...
print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]
```






## Problem 12

Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

```python
def fibonacci(n):
  
print(fibonacci(8)) # [1, 1, 2, 3, 5, 8, 13, 21]
```

## Problem 13

Write a function that takes `n` as a parameter and returns `n` factorial.


```python
def factorial(n):
  ...
print(factorial(5)) # 120
```

## Problem 14

Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

```python
def find_unique(nums):
    ...
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) # [12, 24, 35, 88, 120, 155]
```