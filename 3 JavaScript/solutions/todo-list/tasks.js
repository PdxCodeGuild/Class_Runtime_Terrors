let field = document.getElementById("text-field");
let word = document.getElementById("word");
let btnList = document.getElementById("btn-list");
let btnRemove = document.getElementById("btn-remove");

let list = document.getElementById("list");
let completeList = document.getElementById("completeList");


btnList.addEventListener("click", function (event) {
  let li = document.createElement("li");
  li.innerHTML = field.value;
  list.appendChild(li);
});

btnRemove.addEventListener("click", function (event) {
  let child = list.children[0];
  list.removeChild(child);

  if (list.childElementCount == 0) {
    alert("no more");
  }
});

list.addEventListener("click", function (event) {
  if (event.target.tagName == "LI") {
    event.target.classList.add("strike");
    completeList.appendChild(event.target);
  }
});
