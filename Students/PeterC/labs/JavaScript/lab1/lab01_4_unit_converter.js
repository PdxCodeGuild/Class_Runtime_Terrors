/*
************************************************
Filename: lab01_4_unit_converter.js
Course: Full Stack Developer Evening Bootcamps
Author: Peter Chow, Student
Assignment: Lab 1: Unit converter in JavaScript - Version 4
Date: 12/02/2020
Version 1.0
************************************************

Ask the user for the distance, the starting units, and the units to convert to.
Conversions as elements in a matrix.
*/

const readline = require('readline-sync');
let userInputDist = parseFloat(readline.question('What is the distance? '));
let userInputUnitsIn = (readline.question('What is the input unit (ft, mi, m, or km)? '));
let userInputUnitsOut = (readline.question('What is the output unit (ft, mi, m, or km)? '));

if (userInputUnitsIn == "ft" && userInputUnitsOut == "m") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 0.3048).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "ft" && userInputUnitsOut == "mi") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 0.000189394).toFixed(6)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "ft" && userInputUnitsOut == "km") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 0.0003048).toFixed(6)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "ft" && userInputUnitsOut == "ft") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "m" && userInputUnitsOut == "ft") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist / 0.3048).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "m" && userInputUnitsOut == "mi") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist / 1609.34).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "m" && userInputUnitsOut == "m") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "m" && userInputUnitsOut == "km") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist / 1000).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "mi" && userInputUnitsOut == "ft") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 5280).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "mi" && userInputUnitsOut == "m") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 1609.34).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "mi" && userInputUnitsOut == "km") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 1.60934).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "mi" && userInputUnitsOut == "mi") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "km" && userInputUnitsOut == "ft") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 3280.84).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "km" && userInputUnitsOut == "mi") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 0.621371).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "km" && userInputUnitsOut == "m") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist * 1000).toFixed(4)} in "${userInputUnitsOut}".`)
}
else if (userInputUnitsIn == "km" && userInputUnitsOut == "km") {
    console.log(`You entered: ${userInputDist} for distance, your Input units is in "${userInputUnitsIn}" and your Output unit is ${(userInputDist)} in "${userInputUnitsOut}".`)
}