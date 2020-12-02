/*
************************************************
Filename: lab01_3_unit_converter.js
Course: Full Stack Developer Evening Bootcamps
Author: Peter Chow, Student
Assignment: Lab 1: Unit converter in JavaScript - Version 3
Date: 12/01/2020
Version 1.0
************************************************

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
*/

const readline = require('readline-sync');
let userInputType = (readline.question('Enter the unit Type (feet, miles, meters, kilometers, yards, or inch): '));
let userInputUnits = parseFloat(readline.question('Enter the units to convert: '));

if (userInputType == "feet") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${(userInputUnits * 0.3048).toFixed(4)} meters.`)
}
else if (userInputType == "miles") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${(userInputUnits * 1609.34).toFixed(4)} meters.`)
}
else if (userInputType == "meters") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${userInputUnits} meters.`)
}
else if (userInputType == "kilometers") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${(userInputUnits * 1000.0).toFixed(4)} meters.`)
}
else if (userInputType == "yards") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${(userInputUnits * 0.9144).toFixed(4)} meters.`)
}
else if (userInputType == "inch") {
    console.log(`You entered: ${userInputUnits} ${userInputType}, which is equivalent to ${(userInputUnits *0.0254).toFixed(4)} meters.`)
}