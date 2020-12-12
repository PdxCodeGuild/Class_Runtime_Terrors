const readline = require('readline-sync');

let distance = parseInt(readline.question('\nEnter the original distance: '));
while(true){
    if (/^\d+$/.test(distance)) {
        break;
    }else{
        console.log('\nNot a valid entry. Try agian.')
        distance = parseFloat(readline.question('\nEnter the original distance: '));
    }
}
console.log(`\nThe distance you entered is: ${distance}`);

let origUnits = readline.question('\nEnter the original units(ft, mi, m, or km): ')
origUnits = origUnits.toLowerCase();

while(true){
    if (origUnits != 'ft' && origUnits != 'mi' && origUnits != 'm' && origUnits != 'km') {
        console.log(`\n"${origUnits}" is an invalid entry. \nValid units are ft, mi, m, or km`)
        origUnits = readline.question('\nEnter the original units(ft, mi, m, or km): ')
        origUnits = origUnits.toLowerCase();
    }else{
        console.log(`\nThe units you entered are: "${origUnits}".`)
        break;}
}


if (origUnits == 'ft') {
    calcDist = (distance * 0.3048).toFixed(2)
}else if (origUnits == 'mi') {
    calcDist = (distance * 1609.34).toFixed(2)
}else if (origUnits == 'm') {
    calcDist = distance.toFixed(2)
}else if (origUnits == 'km') {
    calcDist = (distance * 1000).toFixed(2)
}else {
    console.log('If-Then Error!!!')
}


let convertedUnits = readline.question('\nEnter the units you\'re converting to: (ft, mi, m, or km): ')

while(true){
    if (convertedUnits != 'ft' && convertedUnits != 'mi' && convertedUnits != 'm' && convertedUnits != 'km') {
        console.log(`\n"${convertedUnits}" is an invalid entry. \nValid units are ft, mi, m, or km`)
        convertedUnits = readline.question('\nEnter the original units(ft, mi, m, or km): ')
        convertedUnits = convertedUnits.toLowerCase();
    }else{
        console.log(`\nThe units you entered are: "${convertedUnits}".`)
        break;}
}

if (convertedUnits == 'ft') {
    convDist = (calcDist / 0.3048).toFixed(2)
}else if (convertedUnits == 'mi') {
    convDist = (calcDist / 1609.34).toFixed(2)
}else if (convertedUnits == 'm') {
    convDist = calcDist.toFixed(2)
}else if (convertedUnits == 'km') {
    convDist = (calcDist / 1000).toFixed(2)
}else {
    console.log('If-Then Error!!!')
}

console.log(`\n${distance} ${origUnits} convertes to ${convDist} ${convertedUnits}.`)