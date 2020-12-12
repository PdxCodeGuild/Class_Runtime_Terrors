const readline = require('readline-sync');

// global variables 
let winT = [];  // winning ticket; generated once per 100,000
let playT = []; // playing ticket; generated on each iteration
let match = 0;  // stores number of matches in each ticket 
                // reset to 0 for each new ticket generated
let balance = 0; // starting balance
let expenses = 0; // starting expense account
let earnings = 0; // starting earnings account

// generate two lists of 6 random ints from 01:99
    // one list is the Winning Ticket
    // the other list is the Play, which costs $2 per ticket
    // write a function 'pick6()' which generates the random ints
    
function pick6() {
    let ticket =  [];
    for (let i = 0; i < 6; i++) {
        let x = 0; 
        while (x===0) {
            x = Math.floor(Math.random() * 100);
        }
        ticket[i] = x;

    }    
    return(ticket);
}

winT = pick6();
console.log(winT);
// playT = pick6();
// console.log(playT);

// compare the two tickets to find number of matches
    // order matters - the correct digit must be in the correct index
    // write a function 'num_matches(win, play)' <<'win' := winning ticket; 'play' := playing ticket

function num_matches(win, play) {
    match = 0; 
    for (let i = 0; i < 6; i++) {
        if (win[i] === play[i]) {
            match += 1;
        } else {
            continue;
        }
    }
    return(match);
}
// winT = [1,2,3,4,5,6];
// console.log(winT);
// playT = [1,2,3,4,5,6];
// console.log(playT);
// match = num_matches(winT, playT);
// console.log(match);

// determine the winnings
   
function winnings(match) {
    let win = 0;
    if (match === 6) {
        win = 25000000;         // win6 = $25,000,000
    } else if (match === 5) {
        win = 1000000;          // win5 = $1,000,000
    } else if (match === 4) {
        win = 50000;            // win4 = $50,000
    } else if (match === 3) {
        win = 100;              // win3 = $100
    } else if (match === 2) {
        win = 7;                // win2 = $7
    } else if (match === 1) {
        win = 4;                 // win1 = $4
    } else {
        win = 0;
    }
    // console.log(win);
    return(win);
}
// let wins = winnings(match);
// console.log(`$${wins}`);
//balance -= 2;                   // cost of play
//balance = balance + wins; 
//console.log(`$${balance}`);
// TODO: create a loop of 100,000 iterations
    // output the final balance   
for (let i = 0; i < 100000; i++) {
    playT = pick6();
    //console.log(playT);
    match = num_matches(winT, playT);
    let wins = winnings(match);
    //console.log(`$${wins}`);
    //balance -= 2;                   // cost of play
    //balance = balance + wins; 
    //console.log(`$${balance}`);
    expenses -= 2;
    earnings = earnings + wins;
}
let roi = ((earnings - expenses) / expenses)
//console.log(new Intl.NumberFormat({ style: 'currency', currency: 'USD'}).format(balance));
console.log(new Intl.NumberFormat({ style: 'currency', currency: 'USD'}).format(earnings));
console.log(new Intl.NumberFormat({ style: 'currency', currency: 'USD'}).format(expenses));
console.log(roi);