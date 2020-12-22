const cronos = setInterval(theTimer, 1000);

function theTimer() {
    let n = new Date();
    document.getElementById('clock').innerHTML =
    n.toLocaleTimeString();
}