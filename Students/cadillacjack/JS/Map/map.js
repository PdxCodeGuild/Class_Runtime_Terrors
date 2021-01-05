
let mymap = L.map('mapid').setView([45.5051, -122.6750],2);

console.log('Hello')

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiY2FkaWxsYWNqYWNrNDIiLCJhIjoiY2tqOTIwcm9nNDZzdDJxcndzdGtjcXZ2NyJ9.2g2et-TjPYl0NBzJ0dj2nA'
}).addTo(mymap);

const url = "https://jsonplaceholder.typicode.com/users"

axios.get(url)
    .then(function(response){
        console.log(response.data);
        for(i=0;response.data.length>i;i++){
          lat = response.data[i]['address']['geo']['lat']
          lon = response.data[i]['address']['geo']['lng']
          address = response.data[i]['address']
          street = address['street']
          suite = address['suite']
          city = address['city']
          zip = address['zipcode']
          email = response.data[i]['email']
          userName = response.data[i]['name']
          phone = response.data[i]['phone']

        //   console.log(userName)
          let marker = L.marker([lat, lon]).addTo(mymap)
          marker.bindPopup(`<b>${userName}</b><br><p>${street} ${suite}<br>${city}, ${zip}</p>`).openPopup();

          const p = document.createElement('p')
          p.innerText = `
          ${userName} 
          lives at
          ${street} 
          ${suite}`
          let userInfo = document.getElementsByClassName('user-info')
          console.log(userInfo)
          userInfo[0].append(p) 

        }
    })

 .catch (function(error){
    // Handle Error Here
    console.error(error+ ' Its not doing the thing');
})

 