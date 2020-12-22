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
        for(i=0; i<todoList[0].children.length; i++){
            let complete = $('#li'+i)
            // console.log(complete)
            let completed = complete[0].children[0]
            if (completed.checked){
                // console.log("In the ballpark")
                complete.remove()
            }
        } 
    })

    $('#btn-2').on("click", function(){
        for(i=0; i<todoList[0].children.length; i++){
            let complete = $('#li'+i)
            // console.log(complete)
            let completed = complete[0].children[0]
            if (completed.checked){
                // console.log("In the ballpark");
                completed.remove();
                $("#complete").append(complete).css({"text-decoration": "line-through"});
                
            }
        }  
    })
})