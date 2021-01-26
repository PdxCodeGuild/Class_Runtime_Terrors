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

function main() {
    const earnings = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }

    let loops = 99999;
    let costs = 0;
    let gains = 0;
    let i = 0;
    const winner = pick6();
    while (i <= loops) {
        let ticket = pick6();
        costs += 2;
        gains += earnings[num_matches(winner, ticket)];
        i++;
    }
    console.log(`\nwinnings: ${gains}\nexpenses: ${costs}\nroi: ${(gains - costs) / costs}\n`)
}
main()
