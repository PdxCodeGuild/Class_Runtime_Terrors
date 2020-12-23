const readline = require('readline-sync');
winningPicks = []

for (loop1 = 0; loop1 < 6; loop1++) {
    num = Math.floor(Math.random() * 100)
    winningPicks.push(num)
}

console.log(`\nThe winning picks are  ${winningPicks}`)

winnings = 0
expenses = 0
oneMatch = 0
twoMatch = 0
threeMatch = 0
fourMatch = 0
fiveMatch = 0
sixMatch = 0


for (loop2 = 0; loop2 < 100000; loop2++) {  //100,000 time loop
    playerPicks = []
    for (loop3 = 0; loop3 < 6; loop3++){  //loops 6 times to pick player's numbers
        num = Math.floor(Math.random() * 100)
        playerPicks.push(num)
    }
    expenses = expenses - 2

    matches = 0
    for (loop3 = 0; loop3 < 6; loop3++) {  //loops 6 times to compare player's numbers with winning number
        if (playerPicks [loop3] == winningPicks [loop3]) {
            matches++
        }
    }


    if (matches == 1) {
        winnings = winnings + 4
        oneMatch++
    }else if (matches == 2) {
        winnings = winnings + 7
        twoMatch++
    }else if (matches == 3) {
        winnings = winnings + 100
        threeMatch++
    }else if (matches == 4) {
        winnings = winnings + 50000
        fourMatch
    }else if (matches == 5) {
        winnings = winnings + 1000000
        fiveMatch++
    }else if (matches == 6) {
        winnings = winnings + 25000000
        sixMatch++
    }
}

console.log(`\nYour winnings are $${winnings}.`)
console.log(`\nYour expenses are $${expenses}.`)
console.log(`\nYou had ${oneMatch} one match, ${twoMatch} two match, ${threeMatch} three match, ${fourMatch} four match, ${fiveMatch} five match, and ${sixMatch} six match.`)
console.log(`\nYour RTI is ${(winnings - expenses)/expenses}.`)
