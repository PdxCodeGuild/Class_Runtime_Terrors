const readline = require('readline-sync');

/* ver 1
const meter = 0.3048; // 1 meter = 1 foot * 0.3048

let userInput = parseInt(readline.question('Enter a number feet: '));
console.log(`You entered: ${userInput}`);

console.log(`${userInput} ft is ${(userInput * meter).toFixed(4)} m.`)
*/

/* ver 2 

1ft = 0.3048m
1mi = 1609.34m
1m = 1m
1km = 1000m


let meter = {
    ft: 0.3048, 
    mi: 1609.34,
    m: 1.00,
    km: 1000.00
}

let totally = false;
// for (let i = 0; i < meter.length; i++) {
//     console.log(meter[i]);
// }

// for (let met in meter) {
//     console.log("key", met, "value", typeof(meter[met]));
// }

let num = parseInt(readline.question('Enter a number: '));
console.log(`You entered: ${num}`);
let unit = readline.question("Select starting unit (ft, mi, m, km): ");
console.log(`You selected: ${unit}`);
for (let item in meter) {
    if (item === unit) {
        console.log(`${num} ${unit} is ${(num * meter[item]).toFixed(4)} m.`)
        totally = true;
        }
    }
    

if (totally === false) {
    console.log('That unit is not in our dataset.');
} else {
    console.log('Done.')
}
*/ 

/* ver 3 
1in = 0.0254m
1ft = 0.3048m
1yd = 0.9144m
1mi = 1609.34m
1m = 1m
1km = 1000m

let meter = {
    in: 0.0254,
    ft: 0.3048,
    yd: 0.9144, 
    mi: 1609.34,
    m: 1.00,
    km: 1000.00
}

let totally = false;

let num = parseInt(readline.question('Enter a number: '));
console.log(`You entered: ${num}`);
let unit = readline.question("Select starting unit (in, ft, yd, mi, m, km): ");
console.log(`You selected: ${unit}`);
for (let item in meter) {
    if (item === unit) {
        console.log(`${num} ${unit} is ${(num * meter[item]).toFixed(4)} m.`)
        totally = true;
        }
    }
    

if (totally === false) {
    console.log('That unit is not in our dataset.');
} else {
    console.log('Done.')
}
*/

/* ver 4
1in = 0.0254m
1ft = 0.3048m
1yd = 0.9144m
1mi = 1609.34m
1m = 1m
1km = 1000m
*/

let meter = {
    in: 0.0254,
    ft: 0.3048,
    yd: 0.9144, 
    mi: 1609.34,
    m: 1.00,
    km: 1000.00
}

function toMeters(x) {
    // multiply input unit 'x' by meter-conversion unit

}

function toNewUnit(y) {
    // divide input unit 'y' by meter-conversion unit
}

let totally = false;
let x = 0;

let num = parseInt(readline.question('Enter a number: '));
console.log(`You entered: ${num}`);
let unitIn = readline.question("Select starting unit (in, ft, yd, mi, m, km): ");
console.log(`You selected: ${unitIn}`);
let unitOut = readline.question("Select final unit (in, ft, yd, mi, m, km): ");
console.log(`You selected: ${unitOut}`);
for (let item in meter) {
    if (item === unitIn) {
        x = (num * meter[item])
        console.log(`${num} ${unitIn} is ${x.toFixed(4)} m.`)
        totally = true;
        }
    }
    

if (totally === false) {
    console.log('That unit is not in our dataset.');
} 
for (let item in meter) {
    if (item === unitOut) {
        console.log(`${x} m is ${(x / meter[item]).toFixed(4)} ${unitOut}.`)
        totally = true;
        }
    }
    

if (totally === false) {
    console.log('That unit is not in our dataset.');
} 