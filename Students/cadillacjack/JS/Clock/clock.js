let timer = new Date(0,0,0,0)          
let startLap = document.getElementById('startBtn')
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
  let m = checkTime(timer.getMinutes());
  let s = checkTime(timer.getSeconds());
  document.getElementsByClassName('clocked')[0].innerHTML =
  timer.getHours() + ":" + m + ":" + s;
}

setInterval(startClock, 500);

let laps = undefined
startLap.addEventListener('click',function(){    
  laps = setInterval(lapTime, 1000)
})

let stopLap = document.getElementById('stopBtn')
stopLap.addEventListener('click',function(){
  clearTimeout(laps)
  let lap = document.createElement('li')
  lap.id = 'Lap'+lapList[0].children.length
  lap.innerHTML = "Lap "+lapList[0].children.length + ": "+ timer.getHours() + ":" + checkTime(timer.getMinutes()) + ":" + checkTime(timer.getSeconds())
  lapList[0].appendChild(lap)
  console.log(lapList[0].children)    
  timer = new Date(0,0,0,0)
})