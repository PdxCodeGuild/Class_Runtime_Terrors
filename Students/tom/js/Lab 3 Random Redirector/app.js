let websites = ['https://www.bing.com', 'https://www.google.com', 'https://www.yahoo.com', 'https://www.outlook.com']
let redirectSite = websites[Math.floor(Math.random() * websites.length)]


setTimeout(sec5, 1000)
setTimeout(sec4, 2000)
setTimeout(sec3, 3000)
setTimeout(sec2, 4000)
setTimeout(sec1, 5000)
    
function sec5() {
    timeRemaining = 'This page will redirect you randomly to a search page in 5 seconds'
    document.getElementById('header').innerHTML = timeRemaining
}

function sec4() {
    timeRemaining = 'This page will redirect you randomly to a search page in 4 seconds'
    document.getElementById('header').innerHTML = timeRemaining
}

function sec3() {
    timeRemaining = 'This page will redirect you randomly to a search page in 3 seconds'
    document.getElementById('header').innerHTML = timeRemaining
}

function sec2() {
    timeRemaining = 'This page will redirect you randomly to a search page in 2 seconds'
    document.getElementById('header').innerHTML = timeRemaining
}

function sec1() {
    timeRemaining = 'This page will redirect you randomly to a search page in 1 seconds'
    document.getElementById('header').innerHTML = timeRemaining
    window.location.assign(redirectSite)
}