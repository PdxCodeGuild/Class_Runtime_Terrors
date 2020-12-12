/**
 * Let's make a simple todo-list which supports the following operations:
with jquery
add an item to the list
remove an item from the list
mark an item as completed
Removed items should disappear entirely. Completed items should appear at the bottom (or in a separate list) with a line through them. Use vanilla JS to select and manipulate the DOM elements. No jQuery
 */
let count = 0;
const input = document.getElementById("addItem");
const todoList = document.getElementById("todos");
const completedList = document.getElementById("completedTodos");

const handleAddItem = () => input?.value && todoList.appendChild(genTodoItem());
const handleCompleteItem = item => {
  item.removeChild(item.children[1]); // complete button
  item.remove();
  completedList.appendChild(item);
};
const handleRemoveItem = item => item.remove();

const genTodoItem = () => {
  ++count;
  const todo = document.createElement("div");
  todo.innerHTML = input.value;
  input.value = "";
  todo.setAttribute("id", `todo-item-${count}`);
  todo.className = `todo-item ${count % 2 ? "even" : "odd"}`;
  const rmBtn = document.createElement("button");
  rmBtn.innerHTML = "delete";
  rmBtn.onclick = () => handleRemoveItem(todo);
  todo.appendChild(rmBtn);
  const completeBtn = document.createElement("button");
  completeBtn.innerHTML = "complete";
  completeBtn.onclick = () => handleCompleteItem(todo);
  todo.appendChild(completeBtn);
  return todo;
};

$("#addBtn").on("click", () => {
  const $div = genTodoItem();
  $("#todos").append($div);
});
