# :broken_heart: :smiling_imp: Lab1: Python Pain Redux :smiling_imp: :broken_heart:

From the Python labs, redo Pick6, rot13, and the unit converter assignments in JavaScript. The assignment descriptions are given below.

Try not to look at your python code. It is tempting, but you'll get much more out of this if you make an effort to start fresh. If you do get hopelessly stuck though, go look.

To manage the difficutly (and potential frustration) do the labs in the order listed: Unit converte, pick6, then rot13.

For rot13 and the unit converter, you'll need to install the [readline-sync](https://www.npmjs.com/package/readline-sync) package to get user input (nodejs is designed to deal with asynchronous tasks, which makes doing asynchronous things like these assignments a real pain). 

Open up a terminal and create a new directory. 'cd' into that directory and type the following commands into your terminal window to download and install readline-sync:

```
npm init
```
press enter through all the prompts to accept the defaults.

then type:
```
npm install readline-sync
```

after you have installed readline-sync, you need to "import" it using the following expression in your .js files:

```javascript
const readline = require('readline-sync');
```

You can now handle user input in a similar way to how it was done in python. Use the above line and the code below to test thigns out.

```javascript
let userInput = parseInt(readline.question('enter a number: '));
console.log(`you entered: ${userInput}`);
```


# :notebook: unit converter


This lab will involve writing a program that allows the user to convert a number between units.

## Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by **multiplying the input distance by 0.3048**. Below is some sample input/output.

```
> what is the distance in feet? 12
> 12 ft is 3.6576 m
```

## Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

```
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
```

Below is some sample input/output:

```
> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
```

## Version 3

Add support for yards, and inches.

```
1 yard is 0.9144 m
1 inch is 0.0254 m
```

## Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).



|  | ft  | mi  | m  | km  |
|---|----|----|----|---|
|ft|1||0.3048||
|mi||1|1609.34||
|m|1/0.3048|1/1609.34|1|1/1000|
|km|||1000|1|

But instead of filling out that matrix, and checking for each pair of units (`if from_units == 'mi' and to_units == 'km'`), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units **_to_** meters, then convert **_from_** meters to the output units.



Below is some sample input/output:

```
> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
```
<!-- You should first try to write them using JavaScript's `prompt` and `alert` in place of Python's `input` and `print`. Once you have that working, use `input` and `button` elements, with events. You can read the docs on [DOM Manipulation](../docs/09%20-%20DOM%20Manipulation.md) and [Events](../docs/10%20-%20Events.md). You can view a demo [here](https://codepen.io/flux2341/pen/rJpBXe?editors=1010). -->

# :notebook: pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are `[5, 10]` and your ticket numbers are `[10, 5]` you have **0** matches. If the winning numbers are `[5, 10, 2]` and your ticket numbers are `[10, 5, 2]`, you have **1** match. Calculate your net winnings (the sum of all expenses and earnings).

- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000

One function you might write is `pick6()` which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be `num_matches(winning, ticket)` which returns the number of matches between the winning numbers and the ticket.

## Steps

1. Generate a list of 6 random numbers representing the winning tickets
2. Start your balance at 0
2. Loop 100,000 times, for each loop:
3. Generate a list of 6 random numbers representing the ticket
4. Subtract 2 from your balance (you bought a ticket)
5. Find how many numbers match 
6. Add to your balance the winnings from your matches
7. After the loop, print the final balance

## Version 2

The ROI (return on investment) is defined as `(earnings - expenses)/expenses`. Calculate your ROI, print it out along with your earnings and expenses.

# :notebook: rot13

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.


| Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
| ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|


## Version 2 (this is more difficult in JS than in Python, just try it and do your best!)

Allow the user to input the amount of rotation used in the encryption / decryption. They could enter 13, -9, or 12985478439, and your program should still function. Any string encrypted with a positive rotation, should be decrypted with a negative rotation of the same magnitude (i.e., 13/-13, 546543/-546543). The output below demonstrates this:
```
enter the rotation: 32
enter a string: here Is soMe ranDom sTRing 123@^$&#*(&%_#
nkxk Oy yuSk xgtJus yZXotm 123@^$&#*(&%_#

enter the rotation: -32
enter a string: nkxk Oy yuSk xgtJus yZXotm 123@^$&#*(&%_#
here Is soMe ranDom sTRing 123@^$&#*(&%_#
```
Capital letters, spaces, punctuation, and numbers in the string should be preserved.


