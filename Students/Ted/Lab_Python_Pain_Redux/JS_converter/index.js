const readline = require('readline-sync');
// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`);

const kilometers = 1000;
const miles = 1609.34;
const meters = 0.3048;
function lengthToMeters (){
    // let choices = {'feet', 'miles', 'kilometers'};
    let conversion = 0;
    let unit = readline.question('What units is the length in? The choices are: feet, miles or kilometers: ');
    let length = parseFloat(readline.question('What length, including decimals, do you wish to convert to meters?: '));
    if (unit == 'feet'){
        conversion = length * meters;
    }
    else if (unit == 'miles'){
        conversion = length * miles;
    }
    else if (unit == 'kilometers'){
        conversion = length * kilometers;
    }
    // else if unit not in choices{} 
    let answer = conversion.toFixed(3);
    console.log(`${length} ${unit} is equal to ${answer} meters.`);

}
lengthToMeters()
//to get terminal to run this: node index.js