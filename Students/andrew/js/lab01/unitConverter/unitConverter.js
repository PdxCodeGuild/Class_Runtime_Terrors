const readline = require('readline-sync');


function feetToMeters() {
    let measurement = {ft: 0.3048};
    let distance = parseInt(readline.question("Enter a distance in feet."));
    let meters = (distance * measurement['ft']);
    console.log(`${meters}`);

}

function unitToMeters(){
    let measurement = {ft: 0.3048, km:1000, mi:1609.34 };
    let distance = parseInt(readline.question("Enter a distance in meters:"));
    let unit = readline.question("Select a distance unit: ft-feet, km-kilometer or mi-mile.: \n");
    meters = (distance * measurement[unit]);
    console.log(`${distance} ${unit} is ${meters} meters.`);

}

function unitToMetersV3(){
    const measurement = {ft:0.3048, km:1000, mi:1609.34, yd:0.9144, in:0.0254};
    let distance = parseInt(readline.question("Enter a distance: \n"));
    let unit = readline.question("Select a unit for entered distance: type, ft-feet, km-kilometer, yd-yard or in-inch. \n");
    let meters = (distance * measurement[unit]);
    console.log(`${distance} ${unit} is ${meters} meters`);

}
1
function unitToMetersV4(){
    const measurement = {ft:0.3048, km:1000, mi:1609.34, m:1};
    let distance = parseInt(readline.question("Enter a distance: \n"));
    inputUnit = readline.question("Choose a unit: ft-feet, km-kilometer, mi-mile, and m-meter: \n");
    outputUnit = readline.question("Choose a unit to convert to: ft-feet, km-kilometer, mi-mile, and m-meter:");
    meters = (distance * measurement[inputUnit]);
    conversion = meters / measurement[outputUnit];
    console.log(`${distance} ${inputUnit} is ${conversion} ${outputUnit}`);
}


unitToMetersV4();
//feetToMeters();
//unitToMeters();