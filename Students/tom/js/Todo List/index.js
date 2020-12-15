let newItem         = document.getElementById('newItem')
let addToList       = document.getElementById('add-to-list')
let removeFromList  = document.getElementById('remove-from-list')
let incompleteTasks = document.getElementById('incompleteTasks')
let completedTasks  = document.getElementById('completedTasks')

addToList.addEventListener('click', function(){
    addedItem = document.createElement('li') //create list item
    itemText = document.createTextNode(newItem.value) //create a node for the text
    addedItem.appendChild(itemText) //add text to the list item
    incompleteTasks.appendChild(addedItem) //addes item to list
})

removeFromList.addEventListener('click', function(){  //this is for the remove button
    incompleteTasks.removeChild(incompleteTasks.lastElementChild)
})


// move from incomplete to complete
incompleteTasks.addEventListener('click', function(event){
    completedTasks.appendChild(event.target).style.textDecoration='line-through'
})

// move from complete to incomplete 
completedTasks.addEventListener('click', function(event){
    incompleteTasks.appendChild(event.target)
})