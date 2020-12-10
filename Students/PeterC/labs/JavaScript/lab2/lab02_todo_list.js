let input = document.querySelector('#input');
let input_value = input.value;
let toDo = document.getElementById("todo")
let add = document.getElementById('add')
let del = document.getElementById('rem')
let fin = document.getElementById('com')
let done = document.getElementById('done')
add.addEventListener('click', function () {
    let elem = document.createElement('li')
    elem.innerText = input.value
    elem.style.listStyleType = "upper-roman"
    toDo.appendChild(elem)
})
del.addEventListener('click', function () {
    let toDoList = toDo.children
    for (i = 0; i < toDoList.length; i++) {
        if (input.value === toDoList[i].innerHTML) {
            console.log("true")
            toDoList[i].remove()
        }
    }
})
fin.addEventListener('click', function () {
    let toDoList = toDo.children
    for (i = 0; i < toDoList.length; i++) {
        if (input.value === toDoList[i].innerHTML) {
            console.log("true")
            let elem = document.createElement('li')
            elem.style.textDecoration = "line-through"
            elem.innerText = input.value
            elem.style.listStyleType = "lower-greek"
            done.appendChild(elem)
            toDoList[i].remove()
        }
    }
})


