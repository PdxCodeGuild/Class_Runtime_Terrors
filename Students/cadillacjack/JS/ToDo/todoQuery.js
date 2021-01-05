let i = 0
$('#btn-1').on('click', function(){  
    let text = $("#text-field").val()
    let $li = "<li id="+"li"+i+">" +"<input type=checkbox>" + text + "</li>"
    $("#toDoList").append($li)
    let todoList = $("#toDoList")
    console.log(todoList[0])
    $("#text-field").val("")
    i++

    $('#btn-3').on("click", function(){
        let complete = todoList[0].children
        for(i=0; i<complete.length; i++){
            if (complete[i].children[0].checked){
                complete[i].remove()
            }
        } 
    })

    $('#btn-2').on("click", function(){
        let complete = todoList[0].children
        for(i=0; i<complete.length; i++){
            let completed = complete[i].children[0]
            if (completed.checked){
                completed.remove();
                $("#complete").append(complete[i]).css({"text-decoration": "line-through"});
                
            }
        }  
    })
})