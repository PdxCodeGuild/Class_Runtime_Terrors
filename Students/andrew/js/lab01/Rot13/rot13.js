const readline = require('readline-sync');

function rot13(str) {
    
    let input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
    let index = x => input.indexOf(x);
    let translate = y => index(y) > -1 ? output[index(y)] : y;
    return str.split('').map(translate).join('');
    
}

function rot13v2(str){
    let n = parseInt(readline.question("Enter the number of rotations \n"));
    let input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
    output = output.concat(output.slice(0,n));
    console.log(output);
    let index = x => input.indexOf(x);
    let translate = y => index(y) > -1 ? output[index(y) + (n% output.length)] : y;
    return str.split('').map(translate).join('');
    
}


let word = readline.question("Enter a word: \n");
console.log(rot13(word));
console.log(rot13v2(word));



