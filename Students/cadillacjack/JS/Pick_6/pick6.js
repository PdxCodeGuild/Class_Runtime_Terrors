const payout = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

let winnings = 0
let cost = 0
let looper = 100000
while(looper > 0){
    for (let winNum=[],i=0;i<6;++i) winNum[i]=Math.ceil(Math.random()*99);
    for (let myNum=[],i=0;i<6;++i) myNum[i]=Math.ceil(Math.random()*99);
    
    // for (let i=0, win=0; i<6;++i) if (winNum[i]===myNum[i]){win++;};

    function winCheck(){
        let i = 0
        let win = 0
        while (i < 6){
            if (winNum[i] === myNum[i]){
                win++;
            }
            i++;
        }
        return win
    }
    cost += 2
    looper--;
    let won = payout[winCheck()];
    winnings += won
}

console.log(`
You won \$${winnings}
Your ticket purchaces cost you \$${cost}
Your ROI is ${(winnings - cost)/cost * 100}%`)
