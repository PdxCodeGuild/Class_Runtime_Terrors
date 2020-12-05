const readline = require('readline-sync');
winningPicks = []

let loop1
for (loop1 = 0; loop1 < 6; loop1++) {
    num = Math.floor(Math.random() * 100)
    winningPicks.push(num)
}

console.log(`\nThe winning picks are  ${winningPicks}`)

winningsBalance = 0

let loop2
let loop3
// let matches = 0

for (loop2 = 0; loop2 < 100000; loop2++) {  //100,000 time loop
    playerPicks = []
    for (loop3 = 0; loop3 < 6; loop3++){
        num = Math.floor(Math.random() * 100)
        playerPicks.push(num)
    }
    // console.log(`\nThe player's picks are ${playerPicks}`)
    winningsBalance = winningsBalance - 2

    matches = 0
    for (loop3 = 0; loop3 < 6; loop3++) {
        if (playerPicks [loop3] == winningPicks [loop3]) {
            matches++
            // if (matches > 1){
                // console.log(`\nMatches are ${matches}`)
            // }
        }
    }

    if (matches == 1) {
        winningsBalance = winningsBalance + 4
    }else if (matches == 2) {
        winningsBalance = winningsBalance + 7
    }else if (matches == 3) {
        winningsBalance = winningsBalance + 100
    }else if (matches == 4) {
        winningsBalance = winningsBalance + 50000
    }else if (matches == 5) {
        winningsBalance = winningsBalance + 1000000
    }else if (matches == 6) {
        winningsBalance = winningsBalance + 25000000
    }
}

console.log(`\nYour winnings are $${winningsBalance}.`)