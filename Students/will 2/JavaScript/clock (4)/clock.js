var myVar = setInterval(myTimer, 1000);
let count = 00
let btnStart = document.getElementById("start")
btnStart.addEventListener("click", function(){
    var myVar = setInterval(myTimer, 1000);
})
function myTimer() {
  var d = new Date();
  count++
  d.setSeconds(count);
  let dString = `${d.getHours()} ${d.getMinutes()} ${d.getSeconds()}`
  document.getElementById("demo").innerHTML = dString;
}