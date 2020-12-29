let mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidGVkb29naGUiLCJhIjoiY2tqOWk5bWJ3MDE1NzJwcXZvb2FiYXdjOSJ9.jXixlf6Zy6Bq6fbEi_G_CA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  
  .then(json => console.log(json))