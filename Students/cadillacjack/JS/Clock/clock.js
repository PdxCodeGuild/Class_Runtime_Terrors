let timer = new Date(0,0,0,0)          
let startLap = document.getElementById('startBtn')
let stopLap = document.getElementById('stopBtn')
const lapList = document.getElementsByClassName('laps')

function startClock(){
    let now = new Date()
    let h = now.getHours();
    let m = now.getMinutes();
    let s = now.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementsByClassName('now')[0].innerHTML =
    h + ":" + m + ":" + s;
  }
  
  function checkTime(i){
    if (i<10){i = '0'+i}
    return i;
  }
  
  function lapTime(){
    timer.setSeconds(timer.getSeconds()+1)
    let h = checkTime(timer.getHours());
    let m = checkTime(timer.getMinutes());
    let s = checkTime(timer.getSeconds());
    document.getElementsByClassName('clocked')[0].innerHTML =
    h + ":" + m + ":" + s;
  }
  
  setInterval(startClock, 500);
  
  let laps = undefined
  startLap.addEventListener('click',function(){    
    laps = setInterval(lapTime, 1000)
  })
  
  stopLap.addEventListener('click',function(){
    clearTimeout(laps)
    let lap = document.createElement('li')
    lap.id = 'Lap'+lapList[0].children.length
    lap.innerHTML = "Lap "+lapList[0].children.length + ": "+ timer.getHours() + ":" + checkTime(timer.getMinutes()) + ":" + checkTime(timer.getSeconds())
    lapList[0].appendChild(lap)    
    timer = new Date(0,0,0,0)
    document.getElementsByClassName('clocked')[0].innerHTML =
      0+0 + ":" + 0+0 + ":" +0+0;
  })
  
let timerBtn = document.getElementsByClassName('timerBtn')[0]
let timers = undefined
let runTime= undefined
timerBtn.addEventListener('click',function(){
  let tenHour = document.getElementById('tenHour').value
  let hourS = document.getElementById('hour').value
  let tenMin = document.getElementById('tenMin').value
  let minS = document.getElementById('min').value
  let tenSec = document.getElementById('tenSec').value
  let secS = document.getElementById('sec').value
  timers = new Date(0,0,0,tenHour+hourS,tenMin+minS,tenSec+secS);
  runTime = setInterval(timeLeft, 1000);
})

function timeLeft(){
  timers.setSeconds(timers.getSeconds()-1);
  document.getElementsByClassName('timerTime')[0].innerHTML =
  checkTime(timers.getHours()) + ':' + checkTime(timers.getMinutes()) + ':' + checkTime(timers.getSeconds()) ;
  if(checkTime(timers.getHours())==00){
    if(checkTime(timers.getMinutes())==00){
      if(checkTime(timers.getSeconds())==00){
        clearInterval(runTime)
        alert("Times Up")
      }
    }
  }
}
