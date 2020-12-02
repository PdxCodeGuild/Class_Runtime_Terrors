
function getRandomInt(max) 
    {
    return Math.floor(Math.random() * max) + 1;  // returns a random integer from 1 to 99
    }
  
function pick66() 
    {
    let pick6 = [];
    for (let i = 0; i < 6; i++) 
        {
        pick6.push(getRandomInt(99));
        }
    return pick6
    }


function num_matches(wpick6, lpick6)
    {
    let match = 0;

    for(let i = 0; i < 6; i++) 
        {
        if (wpick6[i] === lpick6[i])
            {
            match = match + 1;
            }       
        }
    return match 
    }

function winning(matchreturn)
    {
    if (matchreturn === 1)
        {
        return 4
        }
    else if (matchreturn === 2)
        {
        return 7
        }
    else if (matchreturn === 3)
        {
        return 100
        }
    else if (matchreturn === 4)
        {
        return 50000
        }
    else if (matchreturn === 5)
        {
        return 1000000
        }
    else if(matchreturn === 6)
        {
        return 25000000
        }
    else
        {
        return 0    
        }
    
    }

let startmoney = 0;
let winmoney = 0;
let wpick6 = pick66();
for (let i = 0; i < 100000; i++) 
    {
    startmoney = startmoney + 2;
    lpick6 = pick66();
    let match = (num_matches(wpick6,lpick6));
    winmoney = winmoney + winning(match)
    }

let roi = ((winmoney - startmoney)/startmoney)*100
roi = roi.toFixed(5);

console.log("You just bought 100,000 Tickets at 2 bucks each!")  

console.log("You spent: "+startmoney);
console.log("You won: "+winmoney);

console.log("For a ROI of : "+roi+"%");

