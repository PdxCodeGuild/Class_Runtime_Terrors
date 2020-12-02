const readline = require('readline-sync');
// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`);
const inch = 0.0254;
const yard = 0.9144;
const kilometers = 1000;
const miles = 1609.34;
const feet = 0.3048;
function lengthToLength (){
    let conversion = 0;
    let unit = readline.question('What unit do you wish to convert from? The choices are: feet, miles, inches, yards, meters or kilometers: ');
    let unitout = readline.question('What unit do you wish to convert too? The choices are: feet, miles, inches, yards, meters or kilometers: ');
    let length = parseFloat(readline.question('What length, including decimals, do you wish to convert?: '));
    if (unit == 'feet'){
        conversion = length * feet;
    }
    else if (unit == 'miles'){
        conversion = length * miles;
    }
    else if (unit == 'kilometers'){
        conversion = length * kilometers;
    }
    else if (unit == 'inches'){
        conversion = length * inch;
    }
    else if (unit == 'yards'){
        conversion = length * yard;
    }
    else if (unit == 'meters'){
        conversion = length
    }
    //converting to other than meters
    if (unitout == 'feet'){
        conversion = conversion / feet;
    }
    else if (unitout == 'miles'){
        conversion = conversion / miles;
    }
    else if (unitout == 'kilometers'){
        conversion = conversion / kilometers;
    }
    else if (unitout == 'inches'){
        conversion = conversion / inch;
    }
    else if (unitout == 'yards'){
        conversion = conversion / yard;
    }
    else if (unitout == 'meters'){
        conversion = conversion 
    }
    
    let answer = conversion.toFixed(3);
    console.log(`${length} ${unit} is equal to ${answer} ${unitout}.`);
}
lengthToLength()
//to get terminal to run this: node index.js