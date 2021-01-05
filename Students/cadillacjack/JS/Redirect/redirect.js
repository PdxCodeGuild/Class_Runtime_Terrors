let $body = $('body')
let $words = "<p class= 'text' id= 'hello'> Uh Oh ... Something went wrong</p>"
let $load = "<p class= 'load' id= 'load'>Loading...</p>"

let listed = ['https://cadillacjack42.github.io/cadillacjack.github.io/', 'https://cadillacjack42.github.io/cadillacjack.github.io/bio_index.html',
'https://cadillacjack42.github.io/cadillacjack.github.io/blog_index.html', 'https://cadillacjack42.github.io/cadillacjack.github.io/my_page.html']

// $body.append($words, $load)
// $body.append($load)
// console.log($('#hello')[0].innerText)
// let action = $('#hello')[0].innerText
// for (element of action){
//     let element = $('element')
//     element.animate({left: '250px'})
//     console.log(element)
// }

let num = Math.random() *4
let nums = Math.ceil(num)
let page = listed[nums]
console.log(page)

setTimeout(function() {
    $body.append($words);
}, 1000);
setInterval(function() {
    $body.append($load);
}, 2000);
setTimeout(function() {
    alert("You will be redirected after closing this window");
}, 5000);
setTimeout(function(){
    location.assign(page);
}, 5001);
