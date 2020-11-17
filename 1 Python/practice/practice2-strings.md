
# Practice: Strings

For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```


## Problem 1

Get a string from the user, print out another string, doubling every letter.

```python
def double_letters(word):
  ...
print(double_letters('hello')) # hheelllloo
```

## Problem 2

Return the number of letter occurances in a string.

```python
def count_letter(letter, word):
    ...
print(count_letter('i', 'antidisestablishmentterianism')) # 5
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2
```


## Problem 3

Return the letter that appears the latest in the english alphabet.

```python
def latest_letter(word):
  ...
print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
```


## Problem 4

Write a function that returns the number of occurances of 'hi' in a given string.

```python
def count_hi(text):
  ...
print(count_hi('hihi')) # 2
```

## Problem 5

Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

```python
def snake_case(text):
    ...
print(snake_case('Hello World!')) # hello_world
print(snake_case('This is another example.')) # this_is_another_example
```

## Problem 6

Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

```python
def camel_case(text):
    ...
print(camel_case('Hello World!')) # helloWorld
print(camel_case('This is another example.')) # thisIsAnotherExample
```

## Problem 7

Write a function that converts text to alternating case.

```python
def alternating_case(text):
    ...
print(alternating_case('Hello World!')) # HeLlO WoRlD!
print(alternating_case('This is another example.')) # ThIs iS AnOtHeR ExAmPle.
```

