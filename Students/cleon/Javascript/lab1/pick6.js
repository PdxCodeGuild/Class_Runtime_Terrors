/* 
Cleon
lab 1: Pick 6
11-30-2020
*/

const genRandomNum = () =>{
    //generates random number from 1 to 99 
    return Math.floor(Math.random() * 100) + 1;

}

const genTicket = () => {
    let ticketArray = [];
    for( let i = 0; i < 6; i++ ){
        // pushes random number into array
        ticketArray.push(genRandomNum());
    }
    return ticketArray;
}
// Takes in array of winning ticket and userTicket, compares from matches, return number of matches
const howManyMatches = (wArr, arr) => {
    let numberOfMatch = 0
    for( let i = 0; i < 6; i++ ){
        if(wArr[i] === arr[i]){
            numberOfMatch += 1
        }
    }
    return numberOfMatch;
}
// takes in number of matches returns winnings based on matches 
const prizeWinningsFromMatches = (numberOfMatch) => {
    switch(numberOfMatch){
        case 1: 
            return 4;
        case 2:
            return 7
        case 3:
            return 100;
        case 4:
            return 50000;
        case 5:
            return 1000000;
        case 6:
            return 25000000;
        default:
            return 0;
    }
    
}

let balance = 0;
let ticketsBought = 0;
let earnings = 0;
let expenses = 0;
let roi = 0
const winningTicket = genTicket();

while(ticketsBought < 100000){
    let userTicket = [];
    userTicket = genTicket();
    // balance = balance - 2;
    x = howManyMatches(winningTicket, userTicket);
    balance -= 2;
    expenses +=2;
    balance += prizeWinningsFromMatches(x);
    earnings += prizeWinningsFromMatches(x);
    ticketsBought ++;
}
roi = (earnings - expenses) / expenses;


console.log(`Final Balance = ${balance}`);
console.log(`ROI: (earnings:${earnings} - expenses:${expenses}) / expenses:${expenses} = ${roi}`);
