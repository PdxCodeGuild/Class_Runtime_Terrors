let field = document.getElementById('input_field');
let output = document.getElementById('output');
let add = document.getElementById('add');
let todo = document.getElementById('todo');
let removeItem = document.getElementById('delete');
let done = document.getElementById('done');

add.addEventListener('click', function(){
    
    let bullet = document.createElement('li');
    bullet.innerText = field.value;
    // let todo = document.getElementById('todo');
    todo.appendChild(bullet);
    field.value = '';

})
removeItem.addEventListener('click', function(){
    todo.removeChild(todo.lastElementChild)
})
todo.addEventListener('click', function(){
    let dot = document.querySelector('#todo > li');
    done.appendChild(dot);
})



// let tap = document.getElementById('add');
// tap.addEventListener('click', function(){
//     want = document.createElement('li');
//     console.log(want.appendChild(output.innerHTML));
    
// })


let remove = document.getElementById('delete');

let undone = document.getElementById('todo');

