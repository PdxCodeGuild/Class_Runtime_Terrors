let field = document.getElementById('input_field');
let output = document.getElementById('output');
let add = document.getElementById('add');
let todo = document.getElementById('todo');
let removeItem = document.getElementById('delete');
let done = document.getElementById('done');

add.addEventListener('click', function(){
    let bullet = document.createElement('li');
    
    bullet.innerText = field.value;
    todo.appendChild(bullet);
    field.value = '';
    bullet.addEventListener('click', function(){
        bullet.style.setProperty('text-decoration', 'line-through');
        done.appendChild(bullet);
    })
})
removeItem.addEventListener('click', function(){
    todo.removeChild(todo.lastElementChild)
})






