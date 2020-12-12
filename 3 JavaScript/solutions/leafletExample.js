let mymap = L.map('mapid').setView([51.505, -0.09], 1);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiZ3JlbmtpbCIsImEiOiJjanZ3bWk4bTM0ZGhvNDhtdXI4bDRsemZtIn0.Ky19K25aHrHpN5ljmutQjA'
}).addTo(mymap);

const url = 'https://jsonplaceholder.typicode.com/users';

axios.get(url)
  .then(function (response) {
    // iterate through the objects in the response
    for (let loc of response.data){
        // create a marker for lat lon
        let marker = L.marker([loc.address.geo.lat, loc.address.geo.lng]).addTo(mymap);

        // create a popup for the marker that will show the user's name and address information
        marker.bindPopup(`<b>${loc.name}</b><br><p>${loc.address.street}</p><p>${loc.address.suite}</p>
        <p>${loc.address.city}</p><p>${loc.address.zipcode}</p>`).openPopup();
        
        // create a new li element containing the user's name, username, and email address
         let new_li = document.createElement('li')
         new_li.innerText = `Name: ${loc.name}, Username: ${loc.username}, Email: ${loc.email}`;

        document.querySelector('#info-list').append(new_li);

    }    
  })
  .catch(function (error) {
    console.log(error);
  })