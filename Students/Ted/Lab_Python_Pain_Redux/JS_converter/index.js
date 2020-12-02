const readline = require('readline-sync');
// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`);

const meters = 0.3048;
function feetToMeters (){
    let feet = parseFloat(readline.question('What length, in feet and decimals, do you wish to convert to meters?: '));
    let conversion = feet * meters;
    let answer = conversion.toFixed(3);
    console.log(`${feet}feet is equal to ${answer} meters.`);

}
feetToMeters()
//to get terminal to run this: node index.js