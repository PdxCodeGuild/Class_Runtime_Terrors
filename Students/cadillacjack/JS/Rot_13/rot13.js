const readline = require('readline-sync');
const encodeAlpha = "abcdefghijklmnopqrstuvwxyz"
let secret = readline.question('What is the secret message you would like to encrypt? :\n')
let rot = parseInt(readline.question('What is the level of encryption to use? :\n'))
let rotate = rot%26
let newList= ''
let secretList=''
let capList = encodeAlpha.toUpperCase()

for(i=Math.abs(rotate);i<encodeAlpha.length;i++){
    newList += encodeAlpha[i];
}
for(i=0;i<Math.abs(rotate);i++){
    newList += encodeAlpha[i];
}

function Scramble(){
    i=0
    for(element of secret){
        j = encodeAlpha.indexOf(element.toLowerCase())
        if(newList[j] == undefined){
            secretList+=element
        }
        else if(capList.includes(element)){
            secretList += newList[j].toUpperCase()
        }else{
            secretList += newList[j]
        }
        i++
    }
}

function Unscramble(){
    for(i=0;i<secret.length;i++){
        let j = secret[i]
        let k = newList.indexOf(j.toLowerCase())
        if(encodeAlpha[k]==undefined){
            secretList += secret[i]
        }
        else if(capList.includes(j)){
            secretList += encodeAlpha[k].toUpperCase()
        }else{
            secretList += encodeAlpha[k]
        }
    } 
}

if(rot<0){
    Unscramble()
}else{
    Scramble()
}
console.log(secretList)


let userInput = document.getElementById('secret')
let userRotation = document.getElementById('rot')
let encryptionBtn = document.getElementById('userInput')

userInput.addEventListener('click', function(){
    console.log(userInput.val())
    userInput.val() = ''
})

encryptionBtn.addEventListener('click', function(){
    console.log('Clicky Clicky')
})