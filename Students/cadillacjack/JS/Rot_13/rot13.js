const readline = require('readline-sync');

const encoderRing = "abcdefghijklmnopqrstuvwxyz"

let secret = readline.question('What is the secret message you would like to encrypt? :\n')
let rot = parseInt(readline.question('What is the level of encryption to use? :\n'))
let rotate = Math.abs(13-rot)

for (secretList=[],i=0;i<secret.length;i++) j = secret[i], k = encoderRing.indexOf(j.toLowerCase()), secretList.push(encoderRing[(Math.abs(k+rotate))%26]);

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
console.log(secretList.join(''))