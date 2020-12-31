var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

function myFunction(){
    axios.get('https://jsonplaceholder.typicode.com/users').then(response =>{
        // console.log(response.data)
        return response.data
        })
        .then (data =>{
            // console.log(data)
        let ul = document.getElementById('outputter');
        for (let i = 0; i< data.length; i++) {
            // console.log(data)
            let name = data[i].name;
            let lat = data[i].address.geo; 
            lat =Object.values(lat)
            let long = data[i].address.geo;
            long = Object.values(long);
            var marker = L.marker([`${lat[0]}`,`${long[1]}`]).addTo(mymap); 
            marker.bindPopup( `<b>Name: ${name}</br><b>Long: ${long}</b><br>Lat: ${lat}`).openPopup();
            let li = document.createElement('li');
            li.classList.add('items')
            li.innerText+=`Name: ${name}, Long: ${long}, Lat: ${lat}`
            ul.appendChild(li)
        }
    }).catch(error=>{console.log('error', error)})
}

//without axios but still works 
// function myFunction(){
//     fetch('https://jsonplaceholder.typicode.com/users')
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(data){
//         console.log(data);
//         let ul = document.getElementById('outputter');
//         for (let i = 0; i< data.length; i++) {
//             let name = data[i].name;
//             console.log(name)
//             let lat = data[i].address.geo; //gotta figu how to seperate lat and long
//             lat =Object.values(lat)
//             console.log(lat[0])
//             let long = data[i].address.geo;
//             long = Object.values(long);
//             console.log(long[1])
//             var marker = L.marker([`${lat[0]}`,`${long[1]}`]).addTo(mymap); 
//             marker.bindPopup( `<b>Name: ${name}</br><b>Long: ${long}</b><br>Lat: ${lat}`).openPopup();
//             let li = document.createElement('li');
//             li.innerText+=`Name: ${name}, Long: ${long}, Lat: ${lat}`
//             ul.appendChild(li)
//         }
//     })
// }
