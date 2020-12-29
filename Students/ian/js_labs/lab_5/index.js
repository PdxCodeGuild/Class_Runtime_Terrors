/**
 *
 * any api call
 */

const API_URL = "https://jsonplaceholder.typicode.com/users/";

const fetcher = id =>
  fetch(id ? API_URL + id : API_URL)
    .then(res => res.json())
    .catch(console.log);

const el = document.getElementById("app");
const button = document.getElementById("userBtn");
button.onclick = () =>
  fetcher().then(data => {
    data instanceof Array && data.forEach(u => genUserDom(u));
  });
const createDivWithText = text => {
  const el = document.createElement("div");
  el.innerHTML = text;
  return el;
};
const genUserDom = ({ id, name, username }) => {
  const user = document.createElement("div");
  const _id = createDivWithText(id);
  const _name = createDivWithText(name);
  const _username = createDivWithText(username);
  user.appendChild(_id);
  user.appendChild(_name);
  user.appendChild(_username);
  el.appendChild(user);
};
