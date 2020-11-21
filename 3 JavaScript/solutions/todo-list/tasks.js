// create an array of classes for the new div
// !! THESE ENTRIES ARE SPECIFIC TO MY IMPLEMENTATION
let newDivClasses = ['task incomplete-task'];

// submit task creates a new task from the user's input
// it uses createClassString to assign the div's classes
let submitTask = () => {
    let newDiv = document.createElement('div')
    newDiv.classList = newDivClasses
    newDiv.innerText = document.querySelector('.task-input').value
    document.querySelector('.incomplete-task-list').append(newDiv)
    document.querySelector('.task-input').focus()
    document.querySelector('.task-input').value = ''
}


document.querySelector('.task-submit').addEventListener('click', () => {
    submitTask();
})

// allow the user to use the enter key to submit tasks
document.querySelector('.task-input').addEventListener('keyup', event => {
    if (event.keyCode === 13)
        submitTask();
})

// when clicking on a task in the incomplete tasks list, move that task to the
 // completed tasks list
document.querySelector('.incomplete-task-list').addEventListener('click', event => {
    event.target.classList.remove('incomplete-task');
    event.target.classList.add('completed-task');
    document.querySelector('.completed-task-list').append(event.target);

})

// when clicking on a task in the completed tasks list, remove it form the list
document.querySelector('.completed-task-list').addEventListener('click', event => {
    event.target.remove();
})