let userData = document.getElementById("user_data")

function getUsers() {
    axios
    .get("https://jsonplaceholder.typicode.com/users")
    .then((res) => {
      console.log(res.data[0]["name"]);
      userData.innerHTML = res.data[0]["name"];
    });
  }
  

getUsers();
let map = document.getElementById("mapid")

var mymap = L.map('mapid').setView([51.505, -0.09], 13);
