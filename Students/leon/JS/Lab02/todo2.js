$(document).ready(function(){
    console.log('ready!');
});

$("#add").on("click", function(){
    let $newElem = "<li class='newEl'>" + $("#input").val() + "</li>"

    console.log($newElem)
    $("#todo").append($newElem)
})

$("#todo").on("click", "li", function() {
   //$(this).css({"background-color": "yellowgreen"})
   $(this).toggleClass("selected")
})

$("#todo").on("dblclick", "li", function() {
    let $doneElem = $(this).text()
    console.log($doneElem)
    $("#done").append("<li>" + $doneElem + "</li>").css({"list-style-image": "url(tick.png)"})
    $(this).remove()
})

$("#del").click(function(){
    $("li").remove(".selected")
})

