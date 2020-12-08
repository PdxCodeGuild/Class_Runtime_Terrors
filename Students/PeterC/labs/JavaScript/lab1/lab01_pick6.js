/*
************************************************
Filename: lab01_pick6.js
Course: Full Stack Developer Evening Bootcamps
Author: Peter Chow, Student
Assignment: Lab 1: pick6
Date: 12/03/2020
Version 1.0
************************************************

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
*/

function getRandomInt(max) 
    {
    return Math.floor(Math.random() * max) + 1;  // returns a random integer from 1 to 99
    }
  
function pick6() 
    {
    let pick6 = [];
    for (let i = 0; i < 6; i++) 
        {
        pick6.push(getRandomInt(99));
        }
    return pick6
    }

function num_matches(pick6a, pick6b)
    {
    let match = 0;

    for(let i = 0; i < 6; i++) 
    
        {
        if (pick6c[i] === pick6b[i])
            {
            match = match + 1;
            }       
        }
    return match 
    }

function winning(num_matches)
    {
    if (num_matches === 1)
        {
        return 4
        }
    else if (num_matches === 2)
        {
        return 7
        }
    else if (num_matches === 3)
        {
        return 100
        }
    else if (num_matches === 4)
        {
        return 50000
        }
    else if (num_matches === 5)
        {
        return 1000000
        }
    else if(num_matches === 6)
        {
        return 25000000
        }
    else
        {
        return 0    
        }
    
    }

let startAmt = 0;
let winnings = 0;
let pick6c = pick6();
for (let i = 0; i < 100000; i++) 
    {
    startAmt = startAmt + 2;
    pick6b = pick6();
    let match = (num_matches(pick6c,pick6b));
    winnings = winnings + winning(match)
    }

let roi = ((winnings - startAmt)/startAmt)*100
roi = roi.toFixed(5);

console.log("=== 🍀 Do you feel lucky? 🍀 ===");  
console.log("If you have bought 100,000 🎟️  at $2💵 each.");
console.log("You would of spent a total of: $" + startAmt.toFixed(2) + " 💰");
console.log("You might of won: $"+winnings.toFixed(2) + " 🤑");
console.log("Your ROI would have been : " + (100 - (roi *= -1)).toFixed(3) + "%" + " 📈");
console.log("=== But you didn't buy any 🎫, so you won Zero!😢 ===")