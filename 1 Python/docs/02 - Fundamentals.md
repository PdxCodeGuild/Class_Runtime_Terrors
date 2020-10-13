
# Fundamentals


- [Common Built-in Types](#common-built-in-types)
- [Variables, Objects](#variables-objects)
- [Types](#types)
- [Type Conversion](#type-conversion)
- [Literals](#literals)
- [I/O](#io)
  - [Print](#print)
    - [End](#end)
    - [Multiple Parameters](#multiple-parameters)
    - [Sep](#sep)
  - [Input](#input)
- [Mutability](#mutability)


## Common Built-in Types

For all the built-in types, check the [official docs](https://docs.python.org/3.2/library/stdtypes.html).

- `None` the absence of a value, [null](https://en.wikipedia.org/wiki/Null_pointer)
- `int` integer number
- `float` floating-point number
- `string` text
- `bool` `True` or `False`
- `list` an ordered list of objects
- `set` an unordered collection of unique objects
- `dict` a collection of key-value pairs
- `range` represents a range of numbers


## Variables, Objects

Variables are names given to objects. These allow us to specify the operations we'd like to perform on that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables. You can get an identifier for an object with the function `id()`

```python
x = 5 # x is the variable, 5 is the object
print(id(x))
message = 'hello' # message is the variable, 'hello' is the object
print(id(message))
```
> 512341256<br>
> 231661621

Everything is an object in python, including None, booleans, integers, floats, modules, classes, and functions. This means they can be assigned to variables, passes as parameters to functions, and be put into lists and dictionaries.

## Types

Every object has a type, which can be checked by using the `type()` function.

```python
print(type(None)) # <class 'NoneType'>
print(type(False)) # <class 'boolean'>
print(type(5)) # <class 'int'>
print(type(5.0)) # <class 'float'>
print(type('hello')) # <class 'str'>
print(type(type(5))) # <class 'type'>
```

We can define custom types using [classes](10%20-%20Classes.md).

```python
class Point:
    def __init__(self):
        pass
p = Point()
print(type(p)) # <class '__main__.Point'>
print(type(Point)) # <class 'type'>
```


## Type Conversion

Every class has an initializer, which can be used to create an instance of that class.

```python
print(bool('True')) # True
print(int('5')) # 5
print(float('5.0')) # 5.0
print(str(5)) # '5'
```

## Literals

The easiest way to enter data in your problem is through 'literals', which are called as such because they're *literally* written in the source code.

- bool literals: `True` and `False`
- int literals: `3`, `-20`, `294927`
- float literals: `3.2`, `3.14e-10`
- string literals: `'hello'` and `"world"`
- list literals: `[]`, `[1, 2, 3]`
- dict literals: `{}`, `{'a': 1, 'b': 2}`


## I/O

### Print

Print is a function in python that allows us to print text to the terminal. Each call to `print` will output whatever's passed as a parameter to the console. [python docs](https://docs.python.org/3/library/functions.html#print)

```python
print('hello')
print('world')
```
> hello<br>
> world


#### End

By default, print will have a newline at the end, if you wish to print change that you can specify an `end` parameter.

```python
print('hello', end=' ')
print('world')
```
> hello world

#### Multiple Parameters

If you pass multiple arguments (separated by commas), it'll print them each on a single line with spaces in between. 

```python
name = 'Jane'
score = 97
print("Total score for", name, "is", score)
```
> Total score for Jane is 97

#### Sep

If you want to specify a different separator character (space is default), you can write something like:

```python
name = 'Jane'
score = 97
print("Total score for ", name, " is ", score, sep='_')
```
> Total_score_for_Jane_is_97


### Input

The `input` function allows us to prompt the user for input on the terminal. The string that's passed to it determines what's displayed with the prompt. [python docs](https://docs.python.org/3/library/functions.html#input)

```python
name = input('What is your name? ')
print('Hello', name, '!')

```
> What is your name? Joe<br>
> Hello Joe !


## Mutability

Certain datatypes in Python are **immutable** meaning their values **cannot** be changed. Immutable types include ints, floats, strings, and tuples. This is why string methods like `lower`, `replace` and `strip` return **copies** of the given string. [stack overflow](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)


```python
x = 5
y = x
y += 2
print(x) # 5
print(y) # 7
```

```python
x = ['apples', 'bananas', 'pears']
y = x
y.append('cherries')
print(x) # ['apples', 'bananas', 'pears', 'cherries']
print(y) # ['apples', 'bananas', 'pears', 'cherries']
```

