let time = new Date().getDay();

let currentTime = setInterval(function(){
    let clock = document.getElementById('clock');
    clock.innerHTML = time;

},1000);

