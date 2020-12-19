const readline = require('readline-sync');
let unencryptedMsg = readline.question('enter a string: ');
unencryptedMsgArray = unencryptedMsg.split('')
let letters = 'abcdefghijklmnopqrstuvwxyz';
letterArray = letters.split('')
charArray = 
rotatedLetters = letters.substr(13, 26) + letters.substr(0, 13)
rotatedLettersArray = rotatedLetters.split('')
encryptedArray = []

for (const element of unencryptedMsgArray) {
    if (letters.includes(element)){
        encryptedArray.push(rotatedLettersArray[letterArray.indexOf(element)] + '#');
    } else {
        encryptedArray.push(element)
    }
}
console.log(encryptedArray)
console.log(encryptedArray.join(""))
console.log("code has run")