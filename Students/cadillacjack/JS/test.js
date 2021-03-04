const readline = require('readline-sync');

const encoderRing = "abcdefghijklmnopqrstuvwxyz"

let secret = readline.question('What is the secret message you would like to encrypt? :\n')
let rot = parseInt(readline.question('What is the level of encryption to use? :\n'))
let rotate = Math.abs(13-rot)

// if (rot<0){
//     let rotate = Math.abs(13+rot)
// }else{
//     let rotate = Math.abs(13-rot)
// }

for (secretList=[],i=0;i<secret.length;i++) j = secret[i], k = encoderRing.indexOf(j.toLowerCase()), secretList.push(encoderRing[(Math.abs(k+rotate))%26]);

console.log(secret)

for (element of secret){
    let i= secret.indexOf(element);
    if(element === element.toUpperCase()){
        secretList.splice(i ,1,secretList[i].toUpperCase());  
    }
    if(element === ' '){
        secretList.splice(i ,1,' ');
    }
    if(element == Number(element)){
        secretList.splice(i ,1,element);
    }
}


// for (let winNum=[],i=0;i<6;++i) winNum[i]=Math.ceil(Math.random()*99);
// function Rot13(){
//     let i=0
//     let secretList = []
//     while (i<secret.length){
//         let j = secret[i];
//         let k = encoderRing.indexOf(j);
//         console.log((k+rot)%26);
//         secretList+= encoderRing[(k+rotate)%26];
//         i++
//     }
//     return secretList
// }

// let yup = Rot13()
console.log(secretList.join(''))