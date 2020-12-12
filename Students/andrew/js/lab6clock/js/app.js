

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

function stopwatch(){
    let stopTime = new Date();

    let stopHour = stopTime.getHours();
    let stopMinute = stopTime.getMinutes();
    let stopSec = stopTime.getSeconds();

    let hour = document.getElementById("stophour");
    let minute = document.getElementById("stopmin");
    let second = document.getElementById("stopsec");

    let displayStopwatch = document.getElementById('lap');


}


function reset(){

}

function start(){

}

function stop(){

}

function lap(){

}



stopwatch();