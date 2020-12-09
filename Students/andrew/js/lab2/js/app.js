function addTodo(){
    let ul = document.getElementById("ul-content")
    let li = document.createElement("li");
    let todo = document.getElementById("inputfield").value;
    let text = document.createTextNode(todo);
    li.appendChild(text);
    document.getElementById("ul-content").appendChild(li);
}