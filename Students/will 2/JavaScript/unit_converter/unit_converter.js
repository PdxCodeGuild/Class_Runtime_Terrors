const readline = require('readline-sync');

const distance = readline.question('enter the distance: ');
const convertTo = readline.question('enter the units to conver to: ');

data = distance.split(" ")

conversionFactor = {
    'feet': 0.3048,
    'miles': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'inch': 0.0254,
}

console.log(`${data[0]} ${data[1]} is ${(parseInt(data[0]) * conversionFactor[data[1]]) / conversionFactor[convertTo]} ${convertTo}`)