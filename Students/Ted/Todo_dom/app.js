let field = document.getElementById('input_field');
let output =document.getElementById('output');
let trigger = document.getElementById('trigger');

trigger.addEventListener('click', function(){
    console.log(text_field.value)
})

let add = document.getElementById('add');
let tap = document.getElementById('add');
tap.addEventListener('click', function(){
    want = document.createElement('li');
    want.appendChild(field.value);
})


let remove = document.getElementById('delete');

let undone = document.getElementById('todo');

let done = document.getElementById('done');