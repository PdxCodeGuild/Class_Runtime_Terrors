start = document.getElementById('start')
stopp = document.getElementById('stopp')
reset = document.getElementById('reset')
lap = document.getElementById('lap')

setInterval(clockFunction, 1000)
function clockFunction(){
    currentTime = new Date
    document.getElementById('clock').innerHTML = currentTime.toLocaleTimeString()
}

stopWatchTime = new Date
stopWatchTime.setHours(0,0,0,0)
hours = `${stopWatchTime.getHours()}`.padStart(2,'0')
minutes = `${stopWatchTime.getMinutes()}`.padStart(2,'0')
seconds = `${stopWatchTime.getSeconds()}`.padStart(2,'0')
elapseTime = `${hours}:${minutes}:${seconds}`
document.getElementById('stopwatch').innerHTML = elapseTime

start.addEventListener('click', function(){
    
    stopWatchInterval = setInterval(stopWatch, 1000)
    function stopWatch(){
        stopWatchTime.setSeconds(stopWatchTime.getSeconds() + 1)
        hours = `${stopWatchTime.getHours()}`.padStart(2,'0')
        minutes = `${stopWatchTime.getMinutes()}`.padStart(2,'0')
        seconds = `${stopWatchTime.getSeconds()}`.padStart(2,'0')
        elapseTime = `${hours}:${minutes}:${seconds}`
        document.getElementById('stopwatch').innerHTML = elapseTime
    }
    stopp.addEventListener('click', function(){
        clearInterval(stopWatchInterval)
    })
})

reset.addEventListener('click', function(){
    stopWatchTime.setHours(0,0,0,0)
    document.getElementById('lapTimes').innerHTML = ''
})

lap.addEventListener('click', function(){
    document.getElementById('lapTimes').innerHTML += '<p>' + elapseTime + '</p>'
})