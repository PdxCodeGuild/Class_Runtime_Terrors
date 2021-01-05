

let ms = 0, s = 0, m = 0, rl =1;
let time = 0;
const stopwatchT = document.querySelector('#stopwatch');
const lapsT = document.querySelector('.laps');

const myForm1 = document.getElementById("start");
myForm1.addEventListener("click", (e) =>{
  e.preventDefault();
  start();
})
const myForm2 = document.getElementById("pause");
myForm2.addEventListener("click", (e) =>{
  e.preventDefault();
  pause();
})

const myForm3 = document.getElementById("stop");
myForm3.addEventListener("click", (e) =>{
  e.preventDefault();
  stop();
})
const myForm4 = document.getElementById("restart");
myForm4.addEventListener("click", (e) =>{
  e.preventDefault();
  restart();
})

const myForm5 = document.getElementById("lap");
myForm5.addEventListener("click", (e) =>{
  e.preventDefault();
  lap();
})

const myForm6 = document.getElementById("ResetLap");
myForm6.addEventListener("click", (e) =>{
  e.preventDefault();
 rlap();
})

function start() {
    if (!time){
    time = setInterval(run, 10);
    }
}

function run() {
    
    stopwatchT.innerHTML = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s) + ":" + (ms < 10 ? "0" + ms : ms)
    console.log("1")
    ms++;
    if(ms == 100) {
        ms = 0;
        s++;
    }
    if(s == 60) {
        s = 0;
        m++;
    }
}

function pause() {
    clearInterval(time)
    time = false;
}

function stop() {
    clearInterval(time)
    time = false;
    ms = 0, s = 0, m = 0;
    stopwatchT.innerHTML = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s) + ":" + (ms < 10 ? "0" + ms : ms)

}

function restart() {
    stop();
    start();
}

function lap() {
    if (time){
            let li = document.createElement('li')
            li.innerHTML = "Laps " + rl + " "+ (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s) + ":" + (ms < 10 ? "0" + ms : ms)
            rl++;
            lapsT.appendChild(li);

    }
}

function rlap() {
    lapsT.innerHTML= (" ");
    rl = 1;
}




