$('#btn-list').on('click', function(){
    let $li = "<li>" + $("#text-field").val() + "</li>"
    $("#list").append($li)
  })
  
  //add the event listener to the parent, and look for the child li
  $('#list').on('click','li', function(){
    let $liVal = $(this).text()
    console.log($liVal)
    $('#completeList').append("<li>"+ $liVal + "</li>").css({"text-decoration": "line-through"})
    //equivalent of event target
    $(this).remove()
  })
  
  $('#btn-remove').on('click', function(){
    $('#list li')[0].remove()
  })
  
  
  