let btnAdd = document.getElementById("list_add")
let btnStrike = document.getElementById("list_strike")
let task = document.getElementById("task")
let ulDone = document.getElementById("done")
let ulUndone = document.getElementById("undone")

btnAdd.addEventListener("click", function (event) {
    let li = document.createElement("li");
    li.innerHTML = task.value;
    ulUndone.appendChild(li);
  });

btnStrike.addEventListener("click", function(event) {
    let child = ulUndone.children[0];
    ulUndone.removeChild(child); 
})

ulUndone.addEventListener("click", function(event) {
    if (event.target.tagName == "LI") {
    event.target.classList.add("strike");
    ulDone.appendChild(event.target);
        }
});    