//version 1
// function logger(){
//     let fullDate = new Date(); 
//     let hours =fullDate.getHours();
//     if (hours < 10){
//         hours = `0${hours}`
// }
//     let mins =fullDate.getMinutes();
//     let seconds =fullDate.getSeconds();
//     document.getElementById('hours').innerHTML = `${hours} :`
//     document.getElementById('minutes').innerHTML =`${mins} :`
//     document.getElementById('seconds').innerHTML = seconds
// }

// setInterval(logger, 1000)

//version 2 
function myFunction() {
    let d = new Date();
    let hours = d.setHours(0);
    let mins = d.setMinutes(0);
    let seconds = d.setSeconds(0);
    document.getElementById('hours').innerText = `${d} :`
    // document.getElementById('minutes').innerHTML =`${mins} :`
    // document.getElementById('seconds').innerHTML = seconds  
  }

  setInterval(myFunction,1000)