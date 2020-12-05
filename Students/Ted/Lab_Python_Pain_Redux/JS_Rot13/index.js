

const readline = require('readline-sync');
//enter the rotation:-prompt(accept any interger)
//enter a string-prompt
//output encoded string
//decode with reversed rotation unit

let rotInput = parseInt(readline.question('Enter your rotation number: '));

let stringInput = (readline.question('Enter the string you wish to encode (only lowercase letters): '));

const small = 'abcdefghijklmnopqrstuvwxyz'
// const big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
// const other = '!@#$%^&*()_+'

let sm = small.split('');
// let bg = big.split()
// let otr = other.split()

let strIn = stringInput.split('');

let outArray = []
function innumerate(character){
   
    for (letter in sm){
       
        if (sm[letter] === character){
            
            outArray.push(letter);
        }
    }
    for (letter in outArray){
        letter = letter + rotInput
    }
}
strIn.forEach(innumerate);

let answerArray = []
function codedArray(character){
    // let answerArray = []
    for (letter in sm){
        if (letter === character){
            answerArray.push(letter);
        }
    }
}
// function innumerate(character){
//     let outArray = [];
//     let letter = strIn.indexOf(character);
//    if (letter in sm === character){
//     outArray.push(indexOf(letter));
//    }
//     return outArray
// }
//    else if(letter in big === character){
//     outArray.push(index of letter);ted
//    }
//    else if(letter in other === character){
//     outArray.push(index of letter);
//    }
console.log(outArray)


// function addRot()


//identify index of each in stringInput
//add rot - if greater than 26, -25?
//push to output
//join output -print


    // let rot = rotInput;
    // let stringIn = stringInput;

    // let stringOut = ' ';
    // for each(i=0; i < stringIn.length; i++);
    //     if {
    //         stringOut.push(big[i] + rot);
    //     }
    //     else if (char.toLowerCase()){
    //         stringOut.push(small[i] + rot);
    //     }
    //     else if (char in other){
    //         stringOut.push(other[i] + rot);
    //     }
    // return stringOut;


