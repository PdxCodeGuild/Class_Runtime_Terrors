const readline = require('readline-sync');

function rot13(str) {

    let input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
    let index = x => input.indexOf(x);
    let translate = x => index(x) > -1 ? output[index(x)] : x;
    return str.split('').map(translate).join('');
}


let word = readline.question("Enter a word: \n");

console.log(rot13(word));

//define alphabet
//input a word
// create empty string
//loop and add each rot letter to string
//output rot string