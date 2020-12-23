
let input = document.querySelector('#input');
let input_value = input.value;
let toDo = document.getElementById("todo")
let add = document.getElementById('add')
let del = document.getElementById('del')
let fin = document.getElementById('fin')
let done = document.getElementById('done')
let out = document.getElementById('output')


add.addEventListener('click', function() {
    let newElem = document.createElement('li')
    newElem.innerText = input.value
    newElem.style.listStyleType = "square"
    toDo.appendChild(newElem)
    
   
})

del.addEventListener('click', function() {
    let toDoList = toDo.children
    
    for (i=0; i < toDoList.length; i++) {
        if (input.value === toDoList[i].innerHTML) {
            console.log("true")
            toDoList[i].remove()
        }
    }
})

fin.addEventListener('click', function() {
    let toDoList = toDo.children
    
    for (i=0; i < toDoList.length; i++) {
        if (input.value === toDoList[i].innerHTML) {
            console.log("true")
            let newElem = document.createElement('li')
            newElem.style.textDecoration ="line-through"
            newElem.innerText = input.value
            
            done.appendChild(newElem)
            toDoList[i].remove()
        }
    }

   
})


