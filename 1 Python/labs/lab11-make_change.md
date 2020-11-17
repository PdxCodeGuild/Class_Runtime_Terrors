# Lab 11: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division `//`, which throws away the remainder. `10/3` is `3.333333`, `10//3` is `3`.

```
Welcome to the Change Maker 5000 (tm)
Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny
Would you like make more change? yes
Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies
Would you like make more change? no
Have a good day!
```

## Version 2

Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

```python
coins = [
    ('half-dollar', 50)
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
```