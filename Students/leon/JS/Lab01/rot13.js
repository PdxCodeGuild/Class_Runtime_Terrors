const readline = require('readline-sync');

function rot13(msg, amount) {
   // wrap if necessary
    if (amount < 0) {
        return rot13(msg, amount+26);
    }

    // make output variable
    let output = '';

    // iterate over ea. char. of str plain
    for (let i = 0; i < msg.length; i++) {
        // store char
        let c = msg[i];
        // if within set of letters... 
        if (c.match(/[a-z]/i)) {
            // get its code
            let code = msg.charCodeAt(i);
            // if uppercase letters
            if (code >= 65 && code <= 90) {
                c = String.fromCharCode((((code - 65) + amount) % 26) + 65);
            } 
            // else lowercase
            else if (code >= 97 && code <= 122) {
                c = String.fromCharCode((((code - 97) + amount) % 26) + 97);
            }
        }
        output += c;
    }
    return(output);
}

let userInput = readline.question('Enter a message to encrypt: ');
let userChoice = parseInt(readline.question('Enter a number for rotation: '));
let encrypted = rot13(userInput, userChoice);
console.log(encrypted);