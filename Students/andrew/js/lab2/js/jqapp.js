$('#add-btn').click(function () {

    let text = $('#inputfield').val();
    let div = $('<div class="inner"></div>');
    let li = $('<li></li>').text(text);
    let clear = $('<button/>').text('clear').click(function () {
        $(div).empty();
    });


    let complete = $('<button class="comp"></button>').text("Complete").click(function () {
        li.css('textDecoration', 'line-through');
        $(div).append(clear);
        $(complete).css('backgroundColor', 'red');


    });

    if (text === "") {
        alert("Please enter a TODO in the text field.")
    } else {
        $('#todo').append(div);
        $(div).append(li);
        $(div).append(complete);

    }

});




$('#clear-all').click(function () {
    $('#todo').remove();
    location.reload();
})

