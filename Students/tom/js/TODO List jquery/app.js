$('#add-button').on('click', function(){
    let $list = "<li>" + $("#new-item").val() + "</li>"
    $("#incompleteTasks").append($list)
})
  
$('#remove-button').on('click', function(){
    $('#incompleteTasks li').last().remove()
})

$('#incompleteTasks').on('click','li', function(){
    let $listItem = $(this).text()
    $('#completedTasks').append("<li>"+ $listItem + "</li>").css({"text-decoration": "line-through"})
    $(this).remove()
})

$('#completedTasks').on('click','li', function(){
    let $listItem = $(this).text()
    $('#incompleteTasks').append("<li>"+ $listItem + "</li>")
    $(this).remove()
})
  