const Clock = document.getElementById("clock");
setInterval(() => {
  Clock.innerHTML = new Date().toLocaleTimeString();
}, 1000);

const Stopwatch = document.getElementById("stopwatch"),
  startButton = document.getElementById("start"),
  lapButton = document.getElementById("lap");
let tTime = 0,
  isActive = false;
const fTime = t => (t < 10 ? "0" + Math.floor(t) : Math.floor(t));
const fmtTime = t => `${fTime(t / 3600)}:${fTime(t / 60)}:${fTime(t % 60)}:00`;
const setTime = t => (tTime = t);
const addTime = t => {
  const li = document.createElement("li");
  li.innerHTML = fmtTime(t);
  Stopwatch.appendChild(li);
}

lapButton.onclick = handleLap = () => {
  addTime(tTime);
}
startButton.onclick = () => {
  isActive = !isActive;
  tTime = 0;
  counter.innerHTML = fmtTime(tTime);
  startButton.innerHTML = isActive ? "Stop" : "Start";
}

setInterval(() => {
  if (isActive) {
    setTime(++tTime);
    counter.innerHTML = fmtTime(tTime);
  }
}, 1000);