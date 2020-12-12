const readline = require('readline-sync');

let userdis = parseInt(readline.question('What is your distance? '));
let userunitin = readline.question('What are your input units? ');
let userunitout = readline.question('What are your output units? ');
let base = ""
let out = ""

if (userunitin === 'ft'){
    base = userdis * 0.3048
}else if (userunitin === 'mi'){
    base = userdis * 1609.34
}else if(userunitin === 'm'){
    base = userdis * 1
}else if(userunitin === 'km'){
    base = userdis * 1000
}else if(userunitin === 'yd'){
    base = userdis * 0.9144
}else if(userunitin === 'in'){
    base = userdis * 0.0254
}    

if (userunitout === 'ft'){
    out = base * 1/0.3048
}else if (userunitout === 'mi'){
    out = base * 1/1609.34
}else if(userunitout === 'm'){
    out = base * 1/1
}else if(userunitout === 'km'){
    out = base * 1/1000
}else if(userunitout === 'yd'){
    out = base * 1/0.9144
}else if(userunitout === 'in'){
    out = base * 1/0.0254
}    

console.log("Your answer is : "+ out + " " + userunitout);
