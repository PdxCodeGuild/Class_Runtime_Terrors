const readline = require('readline-sync');

const encoderRing1 = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

const encoderRing2 = [
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m'
]

let secret = readline.question('What is the secret message you would like to encrypt? :\n')
secretList = secret.split('')

let encodeKey = {}

function encoderRing(){
    let i = 0;
    while (i < 26) {
        let j = i
        encodeKey.j = encoderRing1[i], encoderRing2[i]
        i++
    }
}


// encoderRing()
// console.log(encodeKey)
console.log(secretList)