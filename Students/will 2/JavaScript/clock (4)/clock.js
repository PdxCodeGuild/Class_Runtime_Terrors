var myVar = setInterval(theClock, 1000);
let count = 0;
function theClock() {
  var date = new Date();
  date.setHours(0,0,0,0,0);
  count++;
  date.setSeconds(count);
  var hr = date.getHours()
  var min = date.getMinutes();
  var sec = date.getSeconds();
  hr = digits(hr);
  min = digits(min);
  sec = digits(sec);
  x = date.toLocaleTimeString();
  document.getElementById("demo").innerHTML = hr + ":" + min + ":" + sec;
}

function digits(i){
  if (i<10){
    i = "0" + i;
  }
  return i;
}