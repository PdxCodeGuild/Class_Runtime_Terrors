// create an array of classes for the new div
// !! THESE ENTRIES ARE SPECIFIC TO MY IMPLEMENTATION
let newDivClasses = ['task', 'incomplete-task'];

// createClassString creates a string of class names to assign to the newly created
// task element
let createClassString = (cssClassList) => {
    let cssClassString = '';
    for (let cssClass of cssClassList)
        cssClassString = cssClassString += ` ${cssClass}`;

    return cssClassString;
}

// submit task creates a new task from the user's input
// it uses createClassString to assign the div's classes
let submitTask = () => {
    let newDiv = $(`<div class=\"${createClassString(newDivClasses)}\"></div>`).text($('.task-input').val());
    $('.incomplete-task-list').append(newDiv);
    $('.task-input').focus();
    $('.task-input').val('');
}


$('.task-submit').click(() => {
    submitTask();
})

// allow the user to use the enter key to submit tasks
$('.task-input').keyup((event) => {
    if (event.keyCode === 13)
        submitTask();
})

// when clicking on a task in the incomplete tasks list, move that task to the
 // completed tasks list
$('.incomplete-task-list').click((event) => {
    event.target.classList.remove('incomplete-task');
    event.target.classList.add('completed-task');
    $('.completed-task-list').append(event.target);

})

// when clicking on a task in the completed tasks list, remove it form the list
$('.completed-task-list').click((event) => {
    $(event.target).remove();
})