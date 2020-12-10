/* 
Cleon
lab 1: Rot 13
11-30-2020
*/
const readline = require('readline-sync');
let userInput = readline.question('what is the distance in feet? ');


let arrayUserInput = userInput.split('');


const caseLower = "abcdefghijklmnopqrstuz"

const caseUpper ='ABCDEFGHIJKLMNOPQRSTUZ'

const rotation = (arr,shiftRotation) =>{
    let enc = ''
    let tempHoldChar = 0;
    let newNew = 0;
    for( let i = 0; i < arr.length; i++ ){
        if (arr[i].charCodeAt(0)  >= 97 && arr[i].charCodeAt(0) <= 122 ){
            tempHoldChar = arr[i].charCodeAt(0);
            newNew = (tempHoldChar - shiftRotation) % 26  ; // 97 is lower a asii table
            enc += caseLower[newNew];
         } 
        else if(arr[i].charCodeAt(0)  >= 65 && arr[i].charCodeAt(0) <= 90 ){
            tempHoldChar = arr[i].charCodeAt(0)  ;
            newNew = (tempHoldChar - shiftRotation) % 26; 
            enc += caseUpper[newNew];
            }
        else{
            enc += arr[i];
        }
    
    }
    return enc;
}


// let yu = " abcdef g1234 ABCDEFG"
// let py = yu.split('');
// let xxx= ''
// for(let i = 0 ; i <py.length; i++){
//     xxx +=py[i];

// }

console.log(rotation(arrayUserInput,13));
// // let p = ''
// // p +=caseLower[1]
// // p +=caseLower[2]
// // p +=caseLower[3]
// // p +=caseLower[4]
// // p +=yu[1];
// // console.log(p)
// // console.log(yu)
// console.log(py);
// console.log(xxx);