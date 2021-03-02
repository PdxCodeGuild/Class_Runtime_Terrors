
    
function addMe(){   
    let newToDoItem = document.createElement("li");
    let textValue =document.getElementById("inputText" ).value;
    let task = document.createTextNode(textValue);
    newToDoItem.appendChild(task);

    if (textValue === '') {
        alert("You must write something!");
    } 
    else {
        document.getElementById("myUl").appendChild(newToDoItem);
    }

    document.getElementById("inputText" ).value = ""; 

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    newToDoItem.appendChild(span);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
          var div = this.parentElement;
          div.style.display = "none";
        }
    }
}