let urls = ['https://www.w3schools.com/jsref/met_win_settimeout.asp', 
            'https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout', 
           'https://www.sitepoint.com/javascript-settimeout-function-examples/'
           ]

let dakine = Math.floor(Math.random()* urls.length)

let pick = urls[dakine];
console.log(pick)

function myfunc(){
    
  window.location.href = pick
}