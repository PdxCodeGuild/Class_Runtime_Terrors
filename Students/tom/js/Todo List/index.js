let newItem         = document.getElementById('newItem')
let addToList       = document.getElementById('add-to-list')
let removeFromList  = document.getElementById('remove-from-list')
let taskList = document.getElementById('incompleteTasks')

addToList.addEventListener('click', function(){
    console.log(newItem.value)
    addedItem = document.createElement('li') //create list item
    itemText = document.createTextNode(newItem.value) //create a node for the text
    addedItem.appendChild(itemText) //add text to the list item
    document.getElementById('incompleteTasks').appendChild(addedItem) //addes item to list
})

removeFromList.addEventListener('click', function(){  //this is for the remove button
    taskList.removeChild(taskList.lastElementChild)
})

// move from incomplete to complete
tasks = document.getElementById('incompleteTasks').getElementsByTagName('li')
for (let i = 0; i < tasks.length; i++){
    tasks[i].addEventListener('click', function(){
        // addedItem = tasks[i].outerHTML
        // console.log(addedItem)
        // document.getElementById('completedTasks').appendChild(addedItem) //addes item to list
        
        
        addedItem = document.createElement('li') //create list item
        itemText = document.createTextNode(tasks[i].outerText) //create a node for the text
        console.log(tasks)
        addedItem.appendChild(itemText) //add text to the list item
        document.getElementById('completedTasks').appendChild(addedItem) //addes item to list
        taskList.removeChild(tasks[i])
        console.log(tasks)
    })
}

// move from complete to incomplete
// taskList = document.getElementById('completedTasks')
// tasks = document.getElementById('completedTasks').getElementsByTagName('li')
// for (let i = 0; i < tasks.length; i ++){
//     tasks[i].addEventListener('click', function(){
//         addedItem = document.createElement('li') //create list item
//         itemText = document.createTextNode(tasks[i].outerText) //create a node for the text
//         addedItem.appendChild(itemText) //add text to the list item
//         document.getElementById('incompletTasks').appendChild(addedItem) //addes item to list
//         taskList.removeChild(tasks[i])
//     })
// }