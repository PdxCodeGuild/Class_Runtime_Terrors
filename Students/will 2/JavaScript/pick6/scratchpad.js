function pick6(){
    high = 99
    low = 1
    var ticket = []
    for (i = 0; i < 6; i++) 
        ticket.push(Math.floor(Math.random() * (1 + high - low)) + low);
    return ticket;
      
}

function num_matches(winner, ticket){
    var matches = 0;
    for (const item of winner) {
        if (ticket[winner.indexOf(item)] == item)
            matches++;
    }
    return matches
}

const earnings = {
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000,
    }

let gains = 0
let x = 0
while (x < 100){
    let winner = pick6()
    let ticket = pick6()
    console.log(num_matches(winner,ticket))
    console.log(typeof earnings[num_matches(winner, ticket)])
    gains += earnings[num_matches(winner, ticket)]
    console.log(gains)
    x++;
}





