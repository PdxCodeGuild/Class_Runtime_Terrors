var redirect = [
    'https://www.google.com/',
    'https://www.allrecipes.com/recipes/17562/dinner/',
    'https://www.amazon.com/',
    'https://store.steampowered.com/',
    'https://www.java.com/en/download/',
    'http://loli.dance/'
    ]
var screen_1 = document.getElementById('content')
var screen_2 = document.getElementById('overlay')

function makeVisible(){
    screen_1.style.display = 'none'
    screen_2.style.display = 'flex'
}

function countTimer(){ setInterval(timeDown, 1000)}

var timeleft = 4
function timeDown(){
    makeVisible()
  if(timeleft <= 0){
    document.getElementById("countdown").innerHTML = "Hold on, were going places!"
    clickable()
  } else {
    document.getElementById("countdown").innerHTML = timeleft
  }
  timeleft -= 1
}

function clickable(){
    while (true){
        let x = Math.floor(Math.random() * redirect.length)
        console.log(x)
        if (!(redirect[x] === window.location.href)){
            window.location.href = redirect[x]
            break
        }
    }
}