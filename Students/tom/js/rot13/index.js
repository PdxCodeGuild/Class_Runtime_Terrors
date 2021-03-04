const readline = require('readline-sync');
let rotValue = parseInt(readline.question('\nEnter the rotation value: '));
while(true){
    if (/^\d*$/.test(Math.abs(rotValue))) { break;
    }else{console.log('\nNot a valid entry. Try agian.')
        rotValue = parseInt(readline.question('\nEnter the rotation value: '));}
}

console.log(`\nThe rotation value you entered after correction is: ${rotValue}`);

let origString = readline.question('\nEnter a string to encrypt: ');
console.log(`\nThe string you entered is: ${origString}`);
let origArray = origString.split("")

let letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

let origLen = origString.length
rotArray = []
for (i = 0; i < origLen; i++) {
    origLetter = origArray[i]   //iterates through input string to find each letter
    letterLocation = letters.indexOf(origLetter) //finds the index location of each letter
    newLocation = letterLocation + rotValue //adds the rotational value to each index location
    if (newLocation > 0){
        while (newLocation > 52) {
            newLocation = newLocation - 53
        }
    }else if (newLocation < 0) {
        while (newLocation < 0) {
            newLocation = newLocation + 53
        }
    }

    if (origLetter == " ") {
        newLetter = origLetter
    }else{
        newLetter = letters[newLocation] //finds the letter at the new index location
    }
    rotArray.push(newLetter)
}
rotString = rotArray.join("")
console.log(`\nThe encrypted message is "${rotString}"`)