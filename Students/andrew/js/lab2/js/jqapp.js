$('#add-btn').click(function (){
    
    let text = $('#inputfield').val();
    let li = $('<li></li>').text(text);
    let clear = $('<button/>').text('clear').click(function (){
        alert();
    });
    let complete = $('<button id="comp"></button>').text("Complete").click(function (){
        $('#complete').append(li);


    });
   
    if (text === ""){
        alert("Please enter a TODO in the text field.")
    }else{
        
        $('#todo').append(li);
        $(li).append(complete);
    }
    
});

