$(document).ready(function () {
    console.log("Page Loaded... jQuery seems to be functioning.");
});

$('#add-btn').click(function () {
    alert('click');
    let todo = $('#inputfield').val();
    let newEl = $("<li></li>").text()
});


var txt2 = $("<p></p>").text("Text.");   // Create with jQuery
let li = document.createElement("li");
     let dv = document.createElement("div");
     let clearBtn = document.createElement('button');
     let completeBtn = document.createElement('button');
     let todo = document.getElementById("inputfield").value;
     let text = document.createTextNode(todo);