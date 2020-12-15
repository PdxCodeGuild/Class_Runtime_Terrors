const winning_ticket = pick6()

function pick6(){
    let random_list = []
    let loop_2 = 1
    while (loop_2 <= 6){
        random_list.push(Math.floor(Math.random() * 99) + 1)
        loop_2 += 1
    }
    return random_list
}

function num_matches(ticket){
    let matching = 0
    let index = 0
    while (index <=5){
        if (winning_ticket[index] === ticket[index]){
            matching += 1
            index += 1
        } else if (!(winning_ticket[index] === ticket[index])){
            matching += 0
            index += 1
        }
    }
    return matching
}

function matching_value(matched){
    let value = -2
    if (matched === 0){
        return value
    } else if (matched === 1){
        value += 4
        return value
    } else if (matched === 2){
        value += 7
        return value
    } else if (matched === 3){
        value += 100
        return value
    } else if (matched === 4){
        value += 50000
        return value
    } else if (matched === 5){
        value += 1000000
        return value
    } else if (matched === 6){
        value += 25000000
        return value
    }
}

let matched = undefined
let ticket_value = undefined
let ticket = undefined
let value = 0
let loop = 0
let loop_limit = 100000

while (loop < loop_limit){
    ticket = pick6()
    // console.log(loop)
    matched = num_matches(ticket)
    if (matched === 6){
        console.log("JACKPOT!")
    }
    ticket_value = matching_value(matched)
    value += ticket_value
    loop += 1
}
let roi = value / (loop_limit * 2)
if (value < 0){
    console.log(`You have lost \$${value}.`)
    console.log(`Your ROI is: ${roi}`)
}

if (value >= 0){
    console.log(`You have earned \$${value}.`)
    console.log(`Your ROI is: ${roi}`)
}