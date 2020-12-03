let coins = [
    ['half-dollar', 50],
    ['quarter', 25],
    ['dime', 10],
    ['nickel', 5],
    ['penny', 1]
]

function coin_count(value, coin){
    let coins = Math.floor(value / coin[1])
    coins = parseInt(coins)
    return coins
}

function coin_subtract(value, coin_value){
    let new_value = value - coin_value
    return new_value
}

function coin_value(half_dollar, quarter, dime, nickel, penny){
    half_dollar *= 50
    quarter *= 25
    dime *= 10
    nickel *= 5
    let coin_total = half_dollar + quarter + dime + nickel + penny
    return coin_total
}

function play_again(){
    let yes_list = ["yes", "ya", "y"]
    let no_list = ["no", "nah", "n"]
    while (true){
        let replay = prompt("Would you like to make more change?")
        if (yes_list.includes(replay)){
            return true
        } else if (no_list.includes(replay)){
            return false
        } else {
            console.log("Sorry, that was not a supported option")
        }
    }
}

console.log("Welcome to the Change Maker 5000(tm)")

while (true){
    let half_dollar = 0
    let quarter = 0
    let dime = 0
    let nickel = 0
    let penny = 0

    let value = prompt('Enter a dollar amount.')
    // let value = 10
    value = parseFloat(value) * 100

    let coin;
    let i = 1
    for (coin of coins){
        // console.log(coin)
        if (i === 1){
            half_dollar = coin_count(value, coin)
            console.log(half_dollar)
            i += 1
        } else if (i === 2){
            let temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            quarter = coin_count(temp_value, coin)
            i += 1
        } else if (i === 3){
            let temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            dime = coin_count(temp_value, coin)
            i += 1
        } else if (i === 4){
            let temp_value = coin_subtract(value, coin_value(half_dollar, quarter, dime, nickel, penny))
            nickel = coin_count(temp_value, coin)
            i += 1
        } else if (i === 5){
            penny = value - coin_value(half_dollar, quarter, dime, nickel, penny)
            penny = parseInt(penny)
            i += 1
        } else {
            break
        }
    }

    if (half_dollar === 1){
        half_dollar = `${half_dollar} half-dollar,`
    } else if (half_dollar === 0){
        half_dollar = ''
    } else {
        half_dollar = `${half_dollar} half-dollars,`
    }

    if (quarter === 1) {
        quarter = ` ${quarter} quarter,`
    } else if (quarter === 0){
        quarter = ''
    } else {
        quarter = ` ${quarter} quarters,`
    }

    if (dime === 1){
        dime = ` ${dime} dime,`
    } else if (dime === 0){
        dime = ''
    } else {
        dime = ` ${dime} dimes,`
    }

    if (nickel === 1){
        nickel = ` ${nickel} nickel,`
    } else if (nickel === 0){
        nickel = ''
    } else {
        nickel = ` ${nickel} nickels,`
    }

    if (penny === 1){
        penny = ` and ${penny} penny`
    } else if (penny === 0){
        penny = ' and 0 pennies.'
    } else {
        penny = ` and ${penny} pennies.`
    }

    console.log(`Of \$${value / 100}, your change is: ${half_dollar}${quarter}${dime}${nickel}${penny}`)

    let again = play_again()
    if (again === true){
        continue
    } else if (again === false){
        break
    }
}