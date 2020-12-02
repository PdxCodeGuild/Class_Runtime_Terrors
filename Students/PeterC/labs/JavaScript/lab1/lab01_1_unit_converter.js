/*

************************************************
Filename: lab01_1_unit_converter.js
Course: Full Stack Developer Evening Bootcamps
Author: Peter Chow, Student
Assignment: Lab 1: Unit converter in JavaScript - Version 1
Date: 11/30/2020
Version 1.0
************************************************

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. 
So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
*/

const readline = require('readline-sync');
let userInput = parseInt(readline.question('What is the distance in feet?: '));
// console.log(`You entered: ${userInput} feet`);
console.log(`You entered: ${userInput} feet, which is equivalent to ${userInput * 0.3048.toFixed(3)} meters.`);