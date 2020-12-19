let pre = new Date(); 
pre.setHours(0,0,0,0);

let hour = pre.getHours();
let minute = pre.getMinutes();

 
let butstart = document.getElementById('start')
let butlap = document.getElementById('lap')
let clock = document.getElementById('clock')
let midlap = document.getElementById('laplist')

butstart.addEventListener('click',function(){
    let start = setInterval(function() {
    let second = pre.getSeconds();
    second += 1;
    pre.setSeconds(second);
    clock.innerHTML = `${pre.getHours()}:${pre.getMinutes()}:${pre.getSeconds()}:00`;
    }, 1000 )})

butlap.addEventListener('click',function(){
    let loop = document.createElement('li');
    loop.innerHTML = clock.innerHTML;
    midlap.appendChild(loop);

})
