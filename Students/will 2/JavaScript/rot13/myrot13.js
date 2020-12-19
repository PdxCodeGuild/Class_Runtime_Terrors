const readline = require('readline-sync');
let unenOrEn = readline.question('encrypting? y/n ');
let unencryptedMsg = readline.question('enter a string: ');
let letters = 'abcdefghijklmnopqrstuvwxyz';
let rotation = readline.question('enter the rotation: ')
rotation = rotation % 26
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