//Stopwatch Card

const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const lapBtn = document.getElementById("lap");
let dispayClock = document.getElementById("stopwatch");
let list = document.querySelector(".list");
let timeStart = null,
    timeStopped = null,
    stoppedDuration = 0,
    started = null;



function start() {
    if (timeStart === null) {
        timeStart = new Date();
    }

    if (timeStopped != null) {
        stoppedDuration += (new Date() - timeStopped);
    }

    // Diagnostic-> console.log(stoppedDuration);
    started = setInterval(stopWatchCounting, 25);

    // Diagnostic-> console.log("Clicked");

}

function _stop() {
    timeStopped = new Date();
    clearInterval(started)

}


function lap() {
    const newEl = document.createElement("li");
    let text = document.createTextNode(dispayClock.textContent);
    newEl.appendChild(text);
    list.appendChild(newEl);
    // Diagnostic-> console.log("Clicked");
    console.log(list.children.length);
}

function stopWatchCounting() {
    var currentTime = new Date()
        , timeElapsed = new Date(currentTime - timeStart - stoppedDuration)
        , hour = timeElapsed.getHours()
        , min = timeElapsed.getMinutes()
        , sec = timeElapsed.getSeconds()
        , ms = timeElapsed.getMilliseconds().toFixed(0);

    dispayClock.textContent = min + ":" + sec + ": " + ms;
}

function reset() {

    clearInterval(started);
    stoppedDuration = 0;
    timeStart = null;
    timeStopped = null;
    document.getElementById("stopwatch").textContent = "00:00:00";
}

//Not working for some reason?!?
function clear() {

    alert("");
}

//Clock Card
function updateClock() {
    let currentTime = new Date();
    let currentHours = currentTime.getHours();
    let currentMinutes = currentTime.getMinutes();
    let currentSeconds = currentTime.getSeconds();

    let displayClock = document.getElementById("clock")
    let hour = document.getElementById("hour");
    let minute = document.getElementById("min");
    let second = document.getElementById("sec");
    let tod = document.getElementById("timeofday");
    currentMinutes = (currentMinutes < 10 ? "0" : "") + currentMinutes;
    currentSeconds = (currentSeconds < 10 ? "0" : "") + currentSeconds;

    let timeOfDay = (currentTime < 12) ? "AM" : "PM";
    currentHours = (currentHours > 12) ? currentHours - 12 : currentHours;
    currentHours = (currentHours == 0) ? 12 : currentHours;
    currentHours = (currentHours <= 9) ? "0" + currentHours : currentHours;

    let currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds + " " + timeOfDay;
    let timeHours = currentHours;
    let timeMinutes = currentMinutes;
    let timeSeconds = currentSeconds;


    //document.getElementById("clock").firstChild.nodeValue = currentTimeString;
    //displayClock.innerHTML = currentTimeString;

    hour.innerHTML = currentHours;
    minute.innerHTML = currentMinutes;
    second.innerHTML = currentSeconds;
    tod.innerHTML = timeOfDay;

}

