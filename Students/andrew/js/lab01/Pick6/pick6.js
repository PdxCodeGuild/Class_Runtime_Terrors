const readline = require('readline-sync');
const numeral = require('numeral');

let ticketList = [];
let pickList = [];
let matchCount = 0;
let money = 0;

let winnings = 0;

function yourTicket(){
   let num = 6;

   while(num >= 1){
    let randomNumber = Math.random() * 100;
    let pick = ~~randomNumber;
    ticketList.push(pick);
    num--; 
   }
   console.log("Your numbers : " + ticketList);
   return ticketList;
}

function pickSix(){
    let num = 6;

    while(num >= 1){
        let randomNumber = Math.random() * 100;
        let pick = ~~randomNumber;
        pickList.push(pick);
        num--; 
           
    }
    console.log(`Drawn numbers : ${pickList}`)
    return pickList;
}

function earnings(input) {
    let num = input;
    if (num === 1) return winnings += 4;
    if (num === 2) return winnings += 7;
    if (num === 3) return winnings += 100;
    if (num === 4) return winnings += 50000;
    if (num === 5) return winnings += 1000000;
    if (num === 6) return winnings += 25000000;

}


function winChecker() {
    let plays = 100000;
    let currentMatch = 0;
    let tic = yourTicket();
    while (plays > 0) {
        let win = pickSix();
        for (const i in tic) {
            if (win[i] === tic[i]) {
                matchCount++;
                currentMatch++;
                pickList = [];
            } else {
                pickList = [];
            }

        }
        money += 2;
        plays--;
        console.log(` ${plays} : current matches this game: ${currentMatch}`)
        earnings(currentMatch);
        currentMatch = 0;

    }
    console.log("matches : " + matchCount);

    console.log(`Money spent $${money}`);
    console.log(`Cash earned: $${winnings}`);
}

function ROI(){
    return (winnings - money) / money;

}



winChecker();
let returnOnInvestment = numeral(ROI()).format('0.00%');

console.log(`Your return on investment is: ${returnOnInvestment}`);
