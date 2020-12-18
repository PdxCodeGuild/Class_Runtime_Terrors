let pre = new Date(); 
pre.setHours(0,0,0,0);

let hour = pre.getHours();
let minute = pre.getMinutes();
let second = pre.getSeconds();
 

setInterval(function() 1000 {
    second = second +1
    console.log(pre)
})