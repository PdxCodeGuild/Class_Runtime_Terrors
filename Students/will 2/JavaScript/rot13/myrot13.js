const readline = require('readline-sync');

let unencryptedMsg = readline.question('enter a string: ');
let letters = 'abcdefghijklmnopqrstuvwxyz';
let rotation = Math.abs(parseInt(readline.question('enter the rotation: ')))
if (rotation > 26){
    rotation = rotation % 26;
} else {
    rotation = rotation // breaks here-ish...
}
let upperLetters = letters.toUpperCase();
encryptedArray = [];

for (const element of unencryptedMsg) {
    if (letters.includes(element)){
        encryptedArray.push(letters[letters.indexOf(element)+ rotation]);
    } else if (upperLetters.includes(element)){
        encryptedArray.push(upperLetters.toUpperCase()[upperLetters.indexOf(element)+ rotation]);
    } else {
        encryptedArray.push(element);
    }
}
console.log(encryptedArray.join(""))

console.log(letters.indexOf("a") + rotation)