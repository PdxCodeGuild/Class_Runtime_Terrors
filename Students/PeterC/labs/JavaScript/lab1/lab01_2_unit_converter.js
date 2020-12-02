/*
************************************************
Filename: lab01_2_unit_converter.js
Course: Full Stack Developer Evening Bootcamps
Author: Peter Chow, Student
Assignment: Lab 1: Unit converter in JavaScript - Version 2
Date: 12/01/2020
Version 1.0
************************************************

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
*/

const readline = require('readline-sync');
let userInputType = (readline.question('Enter the unit Type (feet, miles, meters, or kilometers): '));
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