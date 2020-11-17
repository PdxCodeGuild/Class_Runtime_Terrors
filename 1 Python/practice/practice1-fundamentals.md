

# Practice 1: Fundamentals

For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```

## Problem 1

Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

```python
def is_even(a):
    ...
print(is_even(5)) # False
print(is_even(6)) # True
```

## Problem 2

Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

```python
def opposite(a, b):
    ...
print(opposite(10, -1)) # True
print(opposite(2, 3)) # False
print(opposite(-1, -1)) # False
```

## Problem 3

Write a function that returns True if a number within 10 of 100.

```python
def near_100(num):
    ...
print(near_100(50)) # False
print(near_100(99)) # True
print(near_100(105)) # True
```

## Problem 4

Write a function that returns the maximum of 3 parameters.

```python
def maximum_of_three(a, b, c):
    ...
print(maximum_of_three(5,6,2)) # 6
print(maximum_of_three(-4,3,10)) # 10
```

## Problem 5

Write a loop to print the powers of 2 from 2^0 to 2^20

```python
def print_powers_2():
  ...
print_powers_2() # 1, 2, 4, 8, 16, 32, ...
```


