

const readline = require('readline-sync');
//enter the rotation:-prompt(accept any interger)
//enter a string-prompt
//output encoded string
//decode with reversed rotation unit

let rotInput = parseInt(readline.question('Enter your rotation number: '));

let stringInput = (readline.question('Enter the string you wish to encode: '));

const small = 'abcdefghijklmnopqrstuvwxyz'
const big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const other = '!@#$%^&*()_+'

let sm = small.split()
let bg = big.split()
let otr = other.split()

let strIn = stringInput.split()
strIn.forEach(innumerate);

function innumerate(character, index){
    
}

//identify index of each in stringInput
//add rot - if greater than 26, -25?
//push to output
//join output -print

function rotx(phrase, codeNumber){ 
    // let rot = rotInput;
    // let stringIn = stringInput;

    let stringOut = ' ';
    for each(i=0; i < stringIn.length; i++);
        if {
            stringOut.push(big[i] + rot);
        }
        else if (char.toLowerCase()){
            stringOut.push(small[i] + rot);
        }
        else if (char in other){
            stringOut.push(other[i] + rot);
        }
    return stringOut;

}
console.log(rotx());