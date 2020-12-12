const readline = require('readline-sync');

let conversionTable = {
    ft : .3048,
    mi : 1609.34,
    m : 1,
    km : 1000,
    yard : .9144,
    inch : .0254
}

let dist = parseInt(readline.question("Enter the distance to be converted : " ))
let unitIn = readline.question("Enter the unit you wish to convert from : ")
let unitOut = readline.question("Enter the unit you wish to convert to : ")

function convert(){
    let unit = dist * conversionTable[unitIn]
    let unit1 = unit / conversionTable[unitOut]
    console.log(`${dist} ${unitIn} is equal to ${unit1.toFixed(5)} ${unitOut}`)
}

convert()