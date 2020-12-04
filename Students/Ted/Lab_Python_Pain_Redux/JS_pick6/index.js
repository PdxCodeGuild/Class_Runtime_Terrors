

function getRandomTicket(){
    let i = 0;
    let l = [];
    while (i < 6){
    let x = Math.floor(Math.random() * 10);
    l.push (x);
    i++;
   }
   return l;
}



function numberMatches(ticket, winner){  
        let i = 0;
        let pay = 0;
        let payout = 0;  
        while (i < 6){
            if ((ticket[i]) === ((winner)[i])){
                pay = pay + 1;
            }
            i ++;
        }
        if (pay == 1){
            payout += 4;
        }else if (pay == 2){
            payout += 7;
        }else if (pay == 3){
            payout += 100;
        }else if (pay == 4){
            payout += 50000;
        }else if (pay == 5){
            payout += 1000000;
        }else if (pay == 6){
            payout += 25000000;
        }       

    return payout;
}

let totalPayout = 0;
let winner = getRandomTicket();

for (let i=0; i < 10; i++){
    let ticket = getRandomTicket();
    let payout = numberMatches(ticket, winner);
    totalPayout = totalPayout + payout -2;
    console.log(`customer ticket ${ticket} payout amount $ ${payout}`)
}

    // function tallyPayout(ticket, payout){
    //         totalPayout = payout + payout;
    //     return totalPayout
    // }

console.log(`winning ticket ${winner}`);
console.log(`number won  is $ ${totalPayout}`);
// console.log(pick6())


// console.log(getRandomInt())
// function winner(){
//     let loto = getRandomInt();
//     return loto;

// function pick6(){
//     let tickets = [];
//     let i = 0;
//     while (i < 10){
//         tickets.push(getRandomTicket());
//         i++; 
//     }
//    return tickets    
// }